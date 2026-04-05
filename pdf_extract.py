"""
PDF Page Extractor
Usage: python pdf_extract.py <source_pdf> <pages> <output_pdf>

Examples:
  python pdf_extract.py input.pdf 1,3,5 output.pdf
  python pdf_extract.py input.pdf 2-5 output.pdf
  python pdf_extract.py input.pdf 1,3-5,8 output.pdf
"""

import sys
import os

try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    print("PyPDF2 is not installed. Install it with:")
    print("  pip install PyPDF2")
    sys.exit(1)


def parse_pages(page_string, total_pages):
    """Parse page specification like '1,3-5,8' into a list of 0-based page indices."""
    pages = set()
    parts = page_string.split(",")

    for part in parts:
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            start = int(start.strip())
            end = int(end.strip())
            if start < 1 or end > total_pages or start > end:
                print(f"Error: Invalid page range '{part}'. PDF has {total_pages} pages.")
                sys.exit(1)
            pages.update(range(start - 1, end))  # convert to 0-based
        else:
            page_num = int(part)
            if page_num < 1 or page_num > total_pages:
                print(f"Error: Page {page_num} is out of range. PDF has {total_pages} pages.")
                sys.exit(1)
            pages.add(page_num - 1)  # convert to 0-based

    return sorted(pages)


def extract_pages(source_path, page_string, output_path):
    """Extract specified pages from source PDF and write to output PDF."""
    if not os.path.exists(source_path):
        print(f"Error: Source file '{source_path}' not found.")
        sys.exit(1)

    reader = PdfReader(source_path)
    total_pages = len(reader.pages)
    print(f"Source: {source_path} ({total_pages} pages)")

    pages = parse_pages(page_string, total_pages)
    print(f"Extracting pages: {', '.join(str(p + 1) for p in pages)}")

    writer = PdfWriter()
    for page_index in pages:
        writer.add_page(reader.pages[page_index])

    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"Saved {len(pages)} page(s) to: {output_path}")


if __name__ == "__main__":
    print("=== PDF Page Extractor ===")
    print()

    # Ask for source PDF
    source_pdf = input("Enter source PDF path: ").strip().strip('"').strip("'")
    if not source_pdf:
        print("Error: No file path provided.")
        sys.exit(1)

    if not source_pdf.lower().endswith(".pdf"):
        source_pdf += ".pdf"

    if not os.path.exists(source_pdf):
        print(f"Error: File '{source_pdf}' not found.")
        sys.exit(1)

    # Show total pages
    reader = PdfReader(source_pdf)
    total_pages = len(reader.pages)
    print(f"  -> Found {total_pages} page(s)")
    print()

    # Ask for pages
    print("Page format examples:")
    print("  Single pages: 1,3,5")
    print("  Page ranges:  2-5")
    print("  Mixed:        1,3-5,8")
    pages = input("Enter pages to extract: ").strip()
    if not pages:
        print("Error: No pages specified.")
        sys.exit(1)
    print()

    # Ask for output filename
    output_pdf = input("Enter output PDF name: ").strip().strip('"').strip("'")
    if not output_pdf:
        # Default name based on source
        base = os.path.splitext(os.path.basename(source_pdf))[0]
        output_pdf = f"{base}_extracted.pdf"
        print(f"  -> Using default: {output_pdf}")
    elif not output_pdf.lower().endswith(".pdf"):
        output_pdf += ".pdf"
    print()

    extract_pages(source_pdf, pages, output_pdf)
