# FileOrg - File Organizer

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

This project is an automated file organizer developed in Python with a graphical user interface using Tkinter. It allows you to select a source folder and a destination folder, automatically categorizing files based on their extensions.

## Features
- **User-friendly graphical interface** using Tkinter
- **Automatic file organization** into categories:
  - 📷 Images
  - 🎥 Videos
  - 🎵 Audio
  - 📄 Documents
  - 📦 Compressed Files
  - ⚙️ Executables
  - 🖥️ 3D Files
- **Folder movement** to a specific category
- **Real-time logging** displayed in the interface

##  Technologies Used
-  **Python 3**
-  **Tkinter** (GUI)
-  `shutil` (file movement)
-  `os` (directory manipulation)

##  How to Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Joullie/fileorg.git
   cd fileorg
## Install dependencies (optional, if using a virtual environment):

pip install -r requirements.txt

Run the program:

python fileorg.py

## How to Create an Executable

If you wish to create a .exe for Windows:

## Install PyInstaller:

pip install pyinstaller

## Generate the executable:

pyinstaller --onefile --windowed fileorg.py

The .exe file will be located in the dist/ folder.

## License
This project is licensed under the MIT License. Feel free to modify and distribute!

## Contributions
Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Create a branch** (`git checkout -b feature-name`)
3. **Make your changes** and commit (`git commit -m "Description"`)
4. **Push to GitHub** (`git push origin feature-name`)
5. **Open a Pull Request** 🚀
