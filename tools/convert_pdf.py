#!/usr/bin/env python3
"""
Convert PDF(s) to Markdown using PyMuPDF4LLM.
Output .md file is placed in the same directory as the input PDF.
Usage: python convert_pdf.py document.pdf [another.pdf ...]
"""

import sys
import os
import pymupdf4llm


def convert_pdf_to_md(pdf_path: str) -> bool:
    """Convert a single PDF to Markdown. Return True on success."""
    if not os.path.exists(pdf_path):
        print(f"❌ Error: File '{pdf_path}' not found.")
        return False

    if not pdf_path.lower().endswith('.pdf'):
        print(f"⚠️  Warning: '{pdf_path}' does not have a .pdf extension, but trying anyway...")

    try:
        md_text = pymupdf4llm.to_markdown(pdf_path, header=False, footer=False)

        base = os.path.splitext(pdf_path)[0]
        md_path = base + '.md'

        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_text)

        print(f"✅ Successfully converted '{pdf_path}' -> '{md_path}'")
        return True

    except Exception as e:
        print(f"❌ Error converting '{pdf_path}': {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_pdf.py <pdf_file1> [pdf_file2 ...]")
        sys.exit(1)

    all_ok = True
    for pdf_file in sys.argv[1:]:
        if not convert_pdf_to_md(pdf_file):
            all_ok = False

    sys.exit(0 if all_ok else 1)
