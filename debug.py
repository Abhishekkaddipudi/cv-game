import cv2
import pytesseract
import numpy as np
import mss
import re
import pyautogui as pgi


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def extract_numbers(text):
    """Extract the first number found in the text using regex."""
    match = re.search(r'\d+', text)
    if match:
        return int(match.group())
    return None
    
with mss.mss() as sct:
    monitor = sct.monitors[1]  # 1 = primary screen

    while True:
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        cropped_img=img[620:680,1200:1300]
        cv2.imshow("Screen", cropped_img)
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
        
        if cv2.waitKey(1) == ord('q'):
            break

cv2.destroyAllWindows()
