#!/usr/bin/env python3
"""
Null-edit alle ArchiMate-relatiepagina's van een model die Categorie:ArchiMateRelationships missen.

Achtergrond: Sjabloon:SmartCoreEpilogue zet deze categorie via #getArchiMateRelationshipType, maar dat
#set/[[Category:...]] draait alleen bij herparsen van de pagina. Bestaande relatiepagina's die vóór de
sjabloonfix zijn geïmporteerd houden hun oude (ontbrekende) categorie tot ze herparst worden. Een
null-edit (exact dezelfde wikitekst terugschrijven) forceert dat herparsen, zonder de inhoud te wijzigen.

Login gebruikt dezelfde credentials als de mediawiki-mcp-server (~/.config/mediawiki-mcp/config.json),
zodat er nergens een wachtwoord in dit script of in de output terechtkomt.

Gebruik:
    python null_edit_relations.py "OverGEMMA/id-7382f25e-04b1-443e-abe5-00fa6e7212c4"          # dry-run
    python null_edit_relations.py "OverGEMMA/id-7382f25e-04b1-443e-abe5-00fa6e7212c4" --execute # schrijft
"""

import argparse
import json
import os
import re
import sys
import time

import requests

DEFAULT_CONFIG = os.path.expanduser("~/.config/mediawiki-mcp/config.json")
TARGET_CATEGORY = "ArchiMateRelationships"


def resolve_env(value: str) -> str:
    """Vervang ${VARNAAM} in een string door de bijbehorende omgevingsvariabele."""
    def sub(m):
        name = m.group(1)
        val = os.environ.get(name)
        if val is None:
            raise SystemExit(f"Omgevingsvariabele {name} is niet gezet (nodig voor login).")
        return val
    return re.sub(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}", sub, value)


def load_credentials(config_path: str, wiki_key: str | None):
    with open(config_path) as f:
        config = json.load(f)
    key = wiki_key or config["defaultWiki"]
    wiki = config["wikis"][key]
    server = wiki["server"].rstrip("/")
    username = resolve_env(wiki["username"])
    password = resolve_env(wiki["password"])
    return server, username, password


def api_request(session: requests.Session, method: str, api_url: str, max_retries: int = 8,
                 backoff: float = 25.0, **kwargs) -> dict:
    """GET/POST met automatische retry bij rate limiting (HTTP 429 of MediaWiki 'ratelimited').

    Dit account hanteert een edit-rate-limit; bij honderden null-edits achter elkaar wordt die
    zeker geraakt. In plaats van te crashen wacht dit gewoon het afkoelvenster af en gaat door.
    """
    for attempt in range(1, max_retries + 1):
        r = session.request(method, api_url, **kwargs)
        if r.status_code == 429:
            wait = float(r.headers.get("Retry-After", backoff))
            print(f"    (HTTP 429, wachten {wait:.0f}s — poging {attempt}/{max_retries})")
            time.sleep(wait)
            continue
        r.raise_for_status()
        data = r.json()
        if isinstance(data, dict) and data.get("error", {}).get("code") == "ratelimited":
            print(f"    (rate limited, wachten {backoff:.0f}s — poging {attempt}/{max_retries})")
            time.sleep(backoff)
            continue
        return data
    raise SystemExit(f"Te vaak rate limited na {max_retries} pogingen — gestopt.")


def login(session: requests.Session, api_url: str, username: str, password: str):
    data = api_request(session, "GET", api_url,
                        params={"action": "query", "meta": "tokens", "type": "login", "format": "json"})
    login_token = data["query"]["tokens"]["logintoken"]

    data = api_request(session, "POST", api_url, data={
        "action": "login",
        "lgname": username,
        "lgpassword": password,
        "lgtoken": login_token,
        "format": "json",
    })
    result = data.get("login", {})
    if result.get("result") != "Success":
        raise SystemExit(f"Login mislukt: {result.get('result')} — {result.get('reason', '')}")


def get_csrf_token(session: requests.Session, api_url: str) -> str:
    data = api_request(session, "GET", api_url,
                        params={"action": "query", "meta": "tokens", "type": "csrf", "format": "json"})
    return data["query"]["tokens"]["csrftoken"]


def find_relationship_pages(session: requests.Session, api_url: str, model: str, limit: int) -> dict:
    """Alle relatiepagina's (herkend aan 'Has source element') van dit model, met hun categorieën.

    Eén #ask-call met ?Categorie als printout i.p.v. een losse call per pagina — anders duurt dit
    bij honderden relaties minutenlang door de netwerklatency per request.
    """
    query = f"[[Occurs in model::{model}]] [[Has source element::+]]|?Categorie|limit={limit}"
    data = api_request(session, "GET", api_url, params={"action": "ask", "query": query, "format": "json"})
    if "error" in data:
        raise SystemExit(f"#ask-fout: {data['error']}")
    return data.get("query", {}).get("results", {})


def missing_target_category(results: dict) -> list[str]:
    missing = []
    for title, info in results.items():
        cats = info.get("printouts", {}).get("Categorie", [])
        names = {c.get("fulltext", "").split(":")[-1] for c in cats if isinstance(c, dict)}
        if TARGET_CATEGORY not in names:
            missing.append(title)
    return missing


def get_wikitext(session: requests.Session, api_url: str, title: str):
    data = api_request(session, "GET", api_url, params={
        "action": "query",
        "prop": "revisions",
        "rvslots": "main",
        "rvprop": "content|timestamp",
        "titles": title,
        "format": "json",
    })
    pages = data["query"]["pages"]
    page = next(iter(pages.values()))
    if "missing" in page:
        return None, None
    rev = page["revisions"][0]
    return rev["slots"]["main"]["*"], rev["timestamp"]


def null_edit(session: requests.Session, api_url: str, csrf_token: str, title: str, text: str, base_timestamp: str):
    data = api_request(session, "POST", api_url, data={
        "action": "edit",
        "title": title,
        "text": text,
        "summary": "Null-edit om herparsing te forceren (Categorie:ArchiMateRelationships-fix toepassen)",
        "bot": 1,
        "nocreate": 1,
        "basetimestamp": base_timestamp,
        "token": csrf_token,
        "format": "json",
    })
    if "error" in data:
        return False, data["error"].get("info", str(data["error"]))
    edit_result = data.get("edit", {}).get("result")
    return edit_result == "Success", edit_result


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("model", help="Paginanaam van het model, bv. OverGEMMA/id-7382f25e-04b1-443e-abe5-00fa6e7212c4")
    parser.add_argument("--execute", action="store_true", help="Daadwerkelijk schrijven. Zonder deze vlag: dry-run.")
    parser.add_argument("--config", default=DEFAULT_CONFIG, help="Pad naar mediawiki-mcp config.json")
    parser.add_argument("--wiki", default=None, help="Wiki-key in de config (default: defaultWiki)")
    parser.add_argument("--limit", type=int, default=2000, help="Max aantal relatiepagina's om op te halen")
    parser.add_argument("--sleep", type=float, default=1.0, help="Seconden pauze tussen edits")
    args = parser.parse_args()

    server, username, password = load_credentials(args.config, args.wiki)
    api_url = f"{server}/api.php"

    session = requests.Session()
    session.headers["User-Agent"] = "GEMMA-null-edit-script/1.0"
    login(session, api_url, username, password)
    print(f"Ingelogd als {username} op {server}")

    print(f"Relatiepagina's zoeken in model {args.model} ...")
    results = find_relationship_pages(session, api_url, args.model, args.limit)
    print(f"  {len(results)} relatiepagina's gevonden totaal")

    missing = missing_target_category(results)
    print(f"  {len(missing)} missen Categorie:{TARGET_CATEGORY}")

    if not missing:
        print("Niets te doen.")
        return

    if not args.execute:
        print("\nDry-run — geen wijzigingen geschreven. Voorbeeldpagina's:")
        for t in missing[:20]:
            print(f"  - {t}")
        if len(missing) > 20:
            print(f"  ... en {len(missing) - 20} meer")
        print("\nVoeg --execute toe om daadwerkelijk null-edits uit te voeren.")
        return

    csrf_token = get_csrf_token(session, api_url)
    ok, failed = 0, []
    for i, title in enumerate(missing, 1):
        text, timestamp = get_wikitext(session, api_url, title)
        if text is None:
            failed.append((title, "pagina niet gevonden"))
            continue
        success, info = null_edit(session, api_url, csrf_token, title, text, timestamp)
        if success:
            ok += 1
        else:
            failed.append((title, info))
        print(f"  [{i}/{len(missing)}] {title}: {'ok' if success else 'FOUT: ' + str(info)}")
        time.sleep(args.sleep)

    print(f"\nKlaar: {ok}/{len(missing)} null-edits gelukt.")
    if failed:
        print(f"{len(failed)} mislukt:")
        for title, info in failed:
            print(f"  - {title}: {info}")


if __name__ == "__main__":
    main()
