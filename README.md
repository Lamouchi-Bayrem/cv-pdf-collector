# FileSorter
<img width="1920" height="1020" alt="Code_opIHUSMmoU" src="https://github.com/user-attachments/assets/f2127971-dc2f-4cb4-aaf8-4d667d1fc8f6" />

**A clean and simple GUI tool to copy files from a directory based on file extension and/or name.**

Perfect for quickly collecting PDFs, images, resumes, invoices, etc.

## Features

- Browse and select source folder
- Filter by file extension (`.pdf`, `.jpg`, `.docx`, ...)
- Optional text filter in filename (case-insensitive)
- Recursive search (includes all subfolders)
- Creates a new `Sorted_...` folder and **copies** the files (originals stay untouched)

## Installation

### From source (recommended for now)

```bash
git clone https://github.com/yourusername/filesorter.git
cd filesorter
pip install -e .

