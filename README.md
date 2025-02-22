# Universal File Converter

A simple and user-friendly GUI application to convert videos, audio files, images, and documents into different formats using FFmpeg and other libraries.

## Features
- Convert video formats (MP4, AVI, MOV, etc.)
- Convert audio formats (MP3, WAV, OGG, etc.)
- Convert image formats (JPG, PNG, etc.)
- Convert document formats (PDF, DOCX, etc.)
- Simple and easy-to-use GUI with file selection and format options

## Prerequisites
### Install Dependencies
Ensure you have the following dependencies installed before running the application:

- **Python 3.x**
- **FFmpeg** (must be installed and added to PATH)
- Required Python packages:
  ```sh
  pip install tkinter pillow moviepy pypandoc customtkinter
  ```

## Installation
Clone this repository and navigate to the project directory:
```sh
git clone https://github.com/yourusername/universal-file-converter.git
cd universal-file-converter
```

## Running the Application
Run the script using Python:
```sh
python converter.py
```

## Usage
1. Click "Browse" to select a file.
2. Choose the desired output format from the dropdown menu.
3. Click "Convert" to start the conversion process.
4. Select the destination and save the converted file.

## FFmpeg Installation Guide
FFmpeg is required for video and audio conversion. Install it as follows:
- **Windows**: Download FFmpeg from [ffmpeg.org](https://ffmpeg.org), extract it, and add the `bin` directory to system PATH.
- **Mac/Linux**: Install via package manager:
  ```sh
  brew install ffmpeg   # macOS (Homebrew)
  sudo apt install ffmpeg  # Ubuntu/Debian
  sudo dnf install ffmpeg  # Fedora
  ```

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [FFmpeg](https://ffmpeg.org) for powerful media conversion tools
- [MoviePy](https://zulko.github.io/moviepy/) for video processing
- [Pillow](https://python-pillow.org) for image processing
- [pypandoc](https://github.com/jgm/pandoc) for document conversion

---
**Developed with ❤️ using Python & CustomTkinter**

