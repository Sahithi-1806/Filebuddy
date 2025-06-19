# FileBuddy 🗂️

FileBuddy is a simple yet powerful Python tool that helps you organize your messy folders by sorting files into categorized subfolders based on their extensions.

## 🚀 Features
- Automatically detects and organizes files into:
  - Images (.png, .jpg, .gif)
  - Documents (.pdf, .docx, .txt)
  - Code files (.py, .html, .js)
  - Videos, Music, Archives, Spreadsheets, and more
- Creates a new folder for each file type category
- Moves unrecognized file types into an "Others" folder
- Works on Windows, Mac, and Linux

## 🔧 Tech Stack
- Python
- `os` module for file handling
- `shutil` for moving files

## 📂 Folder Structure Example
Before:
📁 TestFolder/
├── resume.pdf
├── song.mp3
├── image.png
├── script.py

After running FileBuddy:
📁 TestFolder/
├── Documents/
│ └── resume.pdf
├── Music/
│ └── song.mp3
├── Images/
│ └── image.png
├── Code/
│ └── script.py



## 💻 How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/Sahithi-1806/FileBuddy.git
   cd FileBuddy
Run the script:

bash
Copy code
python filebuddy.py "path/to/your/folder"
Replace "path/to/your/folder" with the actual folder path you want to organize
