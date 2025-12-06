import os
import shutil
import re
from pathlib import Path
import pytesseract
from PIL import Image

# Windows: Set tesseract path if not in PATH
if os.name == 'nt':  # Windows
    tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    if os.path.exists(tesseract_path):
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

class ScreenshotClassifier:
    def __init__(self, screenshots_dir="Screenshots"):
        self.screenshots_dir = Path(screenshots_dir)
        self.categories = {
            "Chats": self.is_chat,
            "Receipts": self.is_receipt,
            "Notes": self.is_note,
            "Memes": self.is_meme
        }
        
    def extract_text(self, image_path):
        """Extract text from image using pytesseract"""
        try:
            img = Image.open(image_path)
            # Use more aggressive OCR config for better text extraction
            custom_config = r'--oem 3 --psm 6'
            text = pytesseract.image_to_string(img, config=custom_config)
            return text
        except Exception as e:
            print(f"Error extracting text from {image_path}: {e}")
            return ""
    
    def is_chat(self, text):
        """Check if screenshot is a chat"""
        text_lower = text.lower()
        time_pattern = r'\d{1,2}:\d{2}\s*(AM|PM|am|pm)'
        has_time = bool(re.search(time_pattern, text))
        chat_indicators = ['message', 'chat', 'replied', 'typing', 'whatsapp', 
                          'telegram', 'messenger', 'online', 'last seen']
        has_chat_words = any(word in text_lower for word in chat_indicators)
        return has_time or has_chat_words
    
    def is_receipt(self, text):
        """Check if screenshot is a receipt"""
        money_pattern = r'(₹|Rs\.?|INR|\$|USD|EUR|£)'
        return bool(re.search(money_pattern, text))
    
    def is_note(self, text):
        """Check if screenshot is a note (long text)"""
        word_count = len(text.split())
        # Also check for note-related keywords
        note_keywords = ['note', 'todo', 'reminder', 'document', 'paragraph']
        has_note_words = any(word in text.lower() for word in note_keywords)
        return word_count > 30 or (word_count > 15 and has_note_words)
    
    def is_meme(self, text):
        """Check if screenshot is a meme (very little text)"""
        # Clean text and count meaningful words
        cleaned_text = text.strip()
        words = [w for w in cleaned_text.split() if len(w) > 1]
        # Only classify as meme if there's 1-4 meaningful words
        return 1 <= len(words) <= 4
    
    def classify_screenshot(self, text):
        """Classify screenshot based on extracted text"""
        # Check specific categories first (order matters)
        if self.is_receipt(text):
            return "Receipts"
        if self.is_chat(text):
            return "Chats"
        if self.is_note(text):
            return "Notes"
        if self.is_meme(text):
            return "Memes"
        return "Uncategorized"
    
    def create_category_folders(self):
        """Create category folders if they don't exist"""
        for category in list(self.categories.keys()) + ["Uncategorized"]:
            folder_path = self.screenshots_dir / category
            folder_path.mkdir(parents=True, exist_ok=True)
    
    def process_screenshots(self):
        """Main function to process all screenshots"""
        if not self.screenshots_dir.exists():
            print(f"Error: {self.screenshots_dir} folder not found!")
            print("Creating Screenshots folder...")
            self.screenshots_dir.mkdir(parents=True, exist_ok=True)
            print("Please add screenshots to the folder and run again.")
            return
        
        # Create category folders
        self.create_category_folders()
        
        # Supported image formats
        image_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff'}
        
        # Get all image files
        screenshots = [f for f in self.screenshots_dir.iterdir() 
                      if f.is_file() and f.suffix.lower() in image_extensions]
        
        if not screenshots:
            print("No screenshots found in the Screenshots folder!")
            return
        
        print(f"Found {len(screenshots)} screenshot(s) to process...\n")
        
        # Process each screenshot
        for screenshot in screenshots:
            print(f"Processing: {screenshot.name}")
            
            # Extract text
            text = self.extract_text(screenshot)
            word_count = len(text.split())
            print(f"  Extracted {word_count} words")
            
            # Debug: show first 150 chars of extracted text
            preview = text.replace('\n', ' ').strip()[:150]
            if preview:
                print(f"  Preview: '{preview}...'")
            else:
                print(f"  Preview: [NO TEXT EXTRACTED]")
            
            # Classify
            category = self.classify_screenshot(text)
            print(f"  Category: {category}")
            
            # Move file
            destination = self.screenshots_dir / category / screenshot.name
            
            # Handle duplicate filenames
            counter = 1
            original_destination = destination
            while destination.exists():
                stem = original_destination.stem
                suffix = original_destination.suffix
                destination = original_destination.parent / f"{stem}_{counter}{suffix}"
                counter += 1
            
            shutil.move(str(screenshot), str(destination))
            print(f"  Moved to: {destination.relative_to(self.screenshots_dir.parent)}\n")

if __name__ == "__main__":
    print("=" * 50)
    print("Screenshot Classifier")
    print("=" * 50 + "\n")
    
    classifier = ScreenshotClassifier()
    classifier.process_screenshots()
    
    print("=" * 50)
    print("Classification complete!")
    print("=" * 50)
