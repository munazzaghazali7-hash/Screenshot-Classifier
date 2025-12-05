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

1. Clone or download this project
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Create a folder named `Screenshots` in the project directory (or it will be created automatically)
2. Add your screenshots to the `Screenshots` folder
3. Run the classifier:
   ```bash
   python screenshot_classifier.py
   ```

4. Your screenshots will be organized into subfolders:
   ```
   Screenshots/
   ├── Chats/
   ├── Receipts/
   ├── Notes/
   ├── Memes/
   └── Uncategorized/
   ```

## Example Output

```
==================================================
Screenshot Classifier
==================================================

Found 5 screenshot(s) to process...

Processing: IMG_001.png
  Extracted 45 words
  Category: Notes
  Moved to: Screenshots/Notes/IMG_001.png

Processing: IMG_002.png
  Extracted 12 words
  Category: Chats
  Moved to: Screenshots/Chats/IMG_002.png

Processing: IMG_003.png
  Extracted 8 words
  Category: Receipts
  Moved to: Screenshots/Receipts/IMG_003.png

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

### "pytesseract.pytesseract.TesseractNotFoundError"
- Make sure Tesseract OCR is installed and added to your system PATH
- On Windows, you may need to specify the path in the script:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```

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
