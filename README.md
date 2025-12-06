# Screenshot Classifier

Automatically classify and organize your screenshots into categories based on their content.

## Features

- **Automatic Text Extraction**: Uses OCR (pytesseract) to read text from screenshots
- **Smart Classification**: Categorizes screenshots into:
  - **Chats**: Screenshots with timestamps (AM/PM) or chat-related keywords
  - **Receipts**: Screenshots containing monetary values (₹, Rs, INR, $, etc.)
  - **Notes**: Screenshots with long text (more than 30 words)
  - **Memes**: Screenshots with minimal text (less than 5 words)
  - **Uncategorized**: Everything else
- **Auto-folder Creation**: Creates category folders automatically
- **Duplicate Handling**: Renames files if duplicates exist
- **Detailed Logging**: Shows what file went where

## Prerequisites

1. **Python 3.7+** installed on your system
2. **Tesseract OCR** installed:
   - **Windows**: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki) and add to PATH
   - **macOS**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

## Installation

1. **Install Tesseract OCR** (required for text extraction):
   - **Windows**: Download installer from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
     - Run the `.exe` installer
     - Default install path: `C:\Program Files\Tesseract-OCR`
     - The script will automatically detect it at this location
   - **macOS**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Add your screenshots to the `Screenshots` folder (created automatically if it doesn't exist)
2. Run the classifier:
   ```bash
   python screenshot_classifier.py
   ```

3. Your screenshots will be automatically organized into subfolders:
   ```
   Screenshots/
   ├── Chats/           # Chat screenshots with timestamps
   ├── Receipts/        # Payment/transaction screenshots
   ├── Notes/           # Long text documents
   ├── Memes/           # Images with minimal text
   └── Uncategorized/   # Everything else
   ```

## Example Output

```
==================================================
Screenshot Classifier
==================================================

Found 6 screenshot(s) to process...

Processing: chat_screenshot.jpg
  Extracted 131 words
  Preview: '7:49 < Untitled < J. Viveka | could've thrown this 7:23 PM...'
  Category: Chats
  Moved to: Screenshots\Chats\chat_screenshot.jpg

Processing: exam_notes.png
  Extracted 230 words
  Preview: 'It can be used in detection of medical problems such as cancer...'
  Category: Notes
  Moved to: Screenshots\Notes\exam_notes.png

Processing: meme.jpg
  Extracted 4 words
  Preview: 'a2 ee ll H...'
  Category: Memes
  Moved to: Screenshots\Memes\meme.jpg

==================================================
Classification complete!
==================================================
```

## Classification Rules

| Category | Rule |
|----------|------|
| Chats | Contains timestamps (AM/PM) or chat keywords |
| Receipts | Contains monetary symbols (₹, Rs, INR, $, USD, EUR, £) |
| Notes | Contains more than 30 words |
| Memes | Contains less than 5 words |
| Uncategorized | Doesn't match any above criteria |

## Troubleshooting

### "tesseract is not installed or it's not in your PATH"
- **Windows**: Download and install Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki)
  - The script automatically checks `C:\Program Files\Tesseract-OCR\tesseract.exe`
  - If installed elsewhere, update line 11 in `screenshot_classifier.py` with your path
- **macOS/Linux**: Install via package manager (brew/apt) and ensure it's in your PATH
- Restart your terminal after installation

### Poor text extraction accuracy
- Ensure screenshots are clear and high resolution
- Tesseract works best with clean, high-contrast text
- Consider preprocessing images (contrast adjustment, noise reduction)

## Customization

You can modify the classification rules in `screenshot_classifier.py`:
- Adjust word count thresholds for Notes/Memes
- Add new categories and classification functions
- Modify regex patterns for better detection

## License

Free to use and modify as needed.
