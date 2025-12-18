# Genshin Artifact Scanner

A high-performance Python tool to capture, analyze, and display Artifact Crit Values (CV) in real-time using OCR and a transparent GUI overlay.

## Features
* **High-Speed Capture**: Uses `BetterCam` for low-latency frame grabbing via Windows Desktop Duplication API.
* **OCR Analysis**: Powered by `Tesseract-OCR` to extract text from specific UI regions.
* **Intelligent Extraction**: Uses Regex to isolate Crit Rate and Crit DMG from other artifact stats.
* **Real-time Overlay**: A transparent, always-on-top `PyQt6` window displays calculations directly over the game.
* **Non-Blocking Input**: Global hotkey support (F9) allows scanning without tabbing out of the game.

## Components & Requirements
### Software Libraries
* **Python 3.11+**
* **BetterCam**: High-performance screen capture.
* **PyTesseract**: Python wrapper for the Tesseract-OCR engine.
* **PyQt6**: For the transparent overlay and UI signals.
* **pynput**: To handle global keyboard hotkeys.

### External Dependencies
* **Tesseract-OCR Engine**: Must be installed on Windows.
* **Windows Administrator Privileges**: Required to capture frames and listen for keys over the game window.

## Future plans    
* integration with personal excel that keeps tracks of character builds    
* additional `PyQt6` window that would display the artifact crit value from the excel sheet allowing for quick comparison of artifacts    
