# Text-to-Speech with Voice Cloning

This project extracts text from PDFs or images, converts the text to speech, and clones a voice from a reference audio file.

## Features
- Extract text from PDFs using `pdfplumber`.
- Extract text from images using `pytesseract`.
- Convert text to speech with voice cloning using Coqui TTS (YourTTS).

## Requirements
- Python 3.8+
- Install dependencies: `pip install -r requirements.txt`

## Usage
1. Place your input file (`example.pdf` or `example_image.png`) in the root directory.
2. Place your reference audio file (`reference_audio.wav`) in the root directory.
3. Run the script:
   ```bash
   python main.py
