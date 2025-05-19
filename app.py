import cv2
import pytesseract
import numpy as np
import mss
import re
import pyautogui as pgi
import time
# Optional: Set path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
region_left = 716
region_top = 6
region_right = 1550
region_bottom = 669

def extract_numbers(text):
    """Extracts all numbers from text and returns list of integers."""
    try:
        return int(text.strip())
    except ValueError:
        print(text)
        return None
    
with mss.mss() as sct:
    monitor = sct.monitors[1]  # Full screen. Change to a region if needed.

    while True:
        # Capture screen
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        cropped_img=img[620:680,1250:1300]
        # Optional: Convert to grayscale to improve OCR
        """
        gray = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)

        # OCR text detection
        text = pytesseract.image_to_string(gray)
        #print(text)
        
        # Extract and analyze numbers
        number = extract_numbers(text)
        if number<92:
            pgi.click(x=1350,y=700)
            #print("clicked")
        else:
            break

        #print(number)
        """
        # Show the screen with overlay
        cv2.imshow("Game Stream Detection", cropped_img)

        # Exit on 'q' key
        if 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
