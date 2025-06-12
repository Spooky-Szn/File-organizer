#file-organizer-bot/
         # Main script
         # Project info
         # Place with messy files (for demo/testing)
import os
import shutil
import argparse
from pathlib import Path

# File categories by extension
File_Types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat"],
    "Scripts": [".py", ".js", ".sh"]
}

def get_category(extension):
    for category, extensions in File_Types.items():
        if extension.lower() in extensions:
            return category
    return "Other"

def organize_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        print(f"Error: Folder '{folder}' does not exist")
        return
    
    for item in folder.iterdir():
        if item.is_file():
            ext = item.suffix.lower()  # Convert to lowercase for case-insensitive comparison
            category = get_category(ext)
            target_folder = folder / category
            target_folder.mkdir(exist_ok=True)
            try:
                shutil.move(str(item), str(target_folder / item.name))
                print(f"Moved: {item.name} to {category}/")
            except Exception as e:
                print(f"Error moving {item.name}: {e}")
    
    print("Organization complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files in a folder by type.")
    parser.add_argument("folder", help="Path to the folder you want to organize")
    args = parser.parse_args()
    organize_folder(args.folder)

    # 🗂️ File Organizer Bot

# A simple Python script that automatically organizes files in a folder by type (images, documents, videos, etc.).



## 📌 What It Does

#- Scans a folder
#- Categorizes files by extension
#- Moves them into subfolders like:
 # - `/Images`
  #- `/Documents`
  #- `/Videos`
 # - `/Other`

#Perfect for cleaning up your messy `Downloads/` folder or organizing workspaces!



## 🚀 How to Use

#Run the script through command prompt. Example: python file_organizer.py "C:\Users\username\OneDrive\Desktop\Python\test_folder"
 #Important note. Use "py" instead of python in the beginning for Windows and filse need to be in the test folder for the script to work.
# The script will automatically scan the folder and move files based on file type
