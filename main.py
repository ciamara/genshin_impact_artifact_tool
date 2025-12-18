import os
os.environ["QT_PA_PLATFORM"] = "windows:dpiawareness=0"
#import ctypes
import bettercam
from pynput import keyboard
import cv2
#from PIL import Image
import pytesseract
import re

import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QFont

from ArtifactOverlay import ArtifactOverlay



def parse_artifact_stats(text):
    
    rate_pattern = r"CRIT Rate.*?\+?(\d+\.?\d*)"
    dmg_pattern = r"CRIT DMG.*?\+?(\d+\.?\d*)"

    rate_match = re.search(rate_pattern, text, re.IGNORECASE)
    dmg_match = re.search(dmg_pattern, text, re.IGNORECASE)

    rate = float(rate_match.group(1)) if rate_match else 0.0
    dmg = float(dmg_match.group(1)) if dmg_match else 0.0

    return rate, dmg

def process_ocr_regions(full_frame):
    #[y_start:y_end, x_start:x_end]
    artifact_type = full_frame[10:45, 7:240]
    artifact_stats = full_frame[185:330, 35:400]
    artifact_owner = full_frame[755:809, 200:360]

    #cv2.imwrite("C:\\Users\\kotel\\OneDrive\\Pulpit\\genshin-artifact-scanner\\type_result.png", artifact_type)
    #cv2.imwrite("C:\\Users\\kotel\\OneDrive\\Pulpit\\genshin-artifact-scanner\\stats_result.png", artifact_stats)
    #cv2.imwrite("C:\\Users\\kotel\\OneDrive\\Pulpit\\genshin-artifact-scanner\\owner_result.png", artifact_owner)

    artifact_type_text = pytesseract.image_to_string(artifact_type, config='--psm 7')
    artifact_stats_text = pytesseract.image_to_string(artifact_stats, config='--psm 6')
    artifact_owner_text = pytesseract.image_to_string(artifact_owner, config='--psm 6')

    return artifact_type_text, artifact_stats_text, artifact_owner_text

def scan_artifact():
    frame = cam.grab(region=region)
    
    if frame is not None:
    
        #cv2.imwrite("C:\\Users\\kotel\\OneDrive\\Pulpit\\genshin-artifact-scanner\\scan_result.png", frame)

        type, stats, owner = process_ocr_regions(frame)
        type = type.strip('\n')
        #print("Artifact type is: " + type)
        owner = owner.strip('\n')
        #print("Artifact owner is: " + owner)

        crit_rate, crit_dmg = parse_artifact_stats(stats)
        #print("Crit rate is: " + str(crit_rate))
        #print("Crit damage is: " + str(crit_dmg))

        crit_value = crit_rate*2 + crit_dmg
        #print("Crit value is: " + str(crit_value))

        overlay.data_received.emit(crit_value)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    global overlay
    overlay = ArtifactOverlay()

    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\kotel\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    
    global cam
    cam = bettercam.create()

    global region
    region = (1450, 160, 1920, 970)

    listener = keyboard.GlobalHotKeys({'<f9>': scan_artifact})
    listener.start() 

    sys.exit(app.exec())