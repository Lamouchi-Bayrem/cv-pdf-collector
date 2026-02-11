#  PDF Collector


Tiny shell script that finds and collects all PDF files containing "cv" (case-insensitive) from your Downloads folder and moves/copies them into a dedicated `~/CV_PDFs` folder.

Perfect for people who regularly download CVs/resumés and want them organized automatically.

## Features

- Case-insensitive search (`*cv*.pdf`, `*CV*.PDF`, `*Curriculum*.pdf`, etc.)
- Creates destination folder if it doesn't exist
- Shows every file it finds and copies
- Final summary with `ls` output
- Safe: uses `-print0` / `read -d ''` for filenames with spaces

## Installation / Usage

```bash
# 1. Clone or download
git clone https://github.com/yourusername/cv-pdf-collector.git
cd cv-pdf-collector

# 2. Make executable
chmod +x find-cvs.sh

# 3. Run it
./find-cvs.sh

# Or run directly without cloning:
bash -c "$(curl -fsSL https://raw.githubusercontent.com/yourusername/cv-pdf-collector/main/find-cvs.sh)"
