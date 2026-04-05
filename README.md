# PDF Page Extractor

A lightweight Python CLI tool to extract specific pages from a PDF file. Select individual pages, ranges, or a mix of both — and save them as a new PDF in seconds.

## ✨ Features

- **Interactive mode** — guided prompts walk you through the process
- **Flexible page selection** — single pages (`1,3,5`), ranges (`2-5`), or mixed (`1,3-5,8`)
- **Input validation** — catches out-of-range pages and invalid formats before processing
- **Auto-naming** — generates a default output filename if you skip it
- **Zero config** — just one dependency, no setup required

## 📦 Requirements

- Python 3.7+
- [PyPDF2](https://pypi.org/project/PyPDF2/)

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/pdfsplitter.git
cd pdfsplitter

# 2. Install the dependency
pip install PyPDF2

# 3. Run it
python pdf_extract.py
```

## 📖 Usage

### Interactive Mode (recommended)

Simply run the script — it will prompt you for everything:

```
$ python pdf_extract.py

=== PDF Page Extractor ===

Enter source PDF path: report.pdf
  -> Found 42 page(s)

Page format examples:
  Single pages: 1,3,5
  Page ranges:  2-5
  Mixed:        1,3-5,8
Enter pages to extract: 10-15

Enter output PDF name: chapter2.pdf

Source: report.pdf (42 pages)
Extracting pages: 10, 11, 12, 13, 14, 15
Saved 6 page(s) to: chapter2.pdf
```

### Page Selection Syntax

| Format      | Example   | Result                      |
|-------------|-----------|-----------------------------|
| Single page | `3`       | Page 3                      |
| Multiple    | `1,3,5`   | Pages 1, 3, and 5           |
| Range       | `2-5`     | Pages 2, 3, 4, and 5        |
| Mixed       | `1,3-5,8` | Pages 1, 3, 4, 5, and 8     |

> **Note:** Pages are 1-indexed (first page = `1`). Duplicates are automatically removed and pages are sorted in order.

## 🗂️ Project Structure

```
pdfsplitter/
├── pdf_extract.py   # Main script
├── README.md
└── .gitignore
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

Free to use, fork, and develop. Contributions are welcome!
