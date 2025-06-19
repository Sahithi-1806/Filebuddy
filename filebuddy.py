import os
import shutil
import sys

# Define file type categories
FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
    "Code": [".py", ".js", ".html", ".css"],
    "Spreadsheets": [".xlsx", ".csv"]
}

def organize_files(source_folder):
    print(f"\nOrganizing files in: {source_folder}\n")
    
    if not os.path.isdir(source_folder):
        print("❌ Invalid path. Please check again.")
        return

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            moved = False

            for folder, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    dest_folder = os.path.join(source_folder, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"✅ Moved: {filename} → {folder}/")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(source_folder, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"📦 Moved: {filename} → Others/")

    print("\n🎉 All files organized successfully!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        source = input("📁 Enter the folder path: ")
    else:
        source = sys.argv[1]

    print(f"📂 Selected folder: {source}")
    print("🔎 Checking files...\n")
    organize_files(source)
