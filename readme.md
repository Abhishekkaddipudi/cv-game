# Game Stream Detection Auto-Clicker

A Python script that captures a region of your screen, performs OCR on a specified sub-region to read numerical values, and automatically sends a click event when a threshold is met. Designed for use with games or other applications where real-time numerical feedback triggers actions.

## Features

* Captures full screen or a custom region using `mss`
* Crops to a smaller area for OCR processing
* Uses Tesseract OCR (`pytesseract`) to read numerical text
* Parses extracted text into integers
* Automatically clicks at specified coordinates using `pyautogui` when the value drops below a threshold
* Real-time display of the cropped region with OpenCV

## Prerequisites

* Python 3.7 or later
* [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system

  * On Windows, note the installation path (e.g., `C:\Program Files\Tesseract-OCR\tesseract.exe`)
  * On macOS, you can install via Homebrew:

    ```bash
    brew install tesseract
    ```
* Python libraries:

  ```bash
  pip install mss opencv-python pytesseract pyautogui numpy
  ```

## Repository Structure

```
.github/             # GitHub workflows (if any)
README.md            # This file
auto_clicker/        # Main script directory
  └── detect_and_click.py  # Core Python script
```

## Configuration

You can adjust the following settings in `detect_and_click.py`:

* **Screen capture region**

  ```python
  region_left = 716
  region_top = 6
  region_right = 1550
  region_bottom = 669
  ```

  Change these values to define the area to capture.

* **OCR sub-region (crop)**

  ```python
  cropped_img = img[620:680, 1250:1300]
  ```

  Modify the pixel coordinates of the slice to target the on-screen number.

* **Threshold and click coordinates**

  ```python
  if number < 92:
      pgi.click(x=1350, y=700)
  ```

  Set your own threshold and the click position where the mouse should click.

* **Tesseract executable path**

  ```python
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```

  Update this if Tesseract is installed elsewhere on your system.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/game-stream-detector.git
   cd game-stream-detector/auto_clicker
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Edit `detect_and_click.py` to configure regions, thresholds, and paths.
4. Run the script:

   ```bash
   python detect_and_click.py
   ```
5. Press `q` in the OpenCV window to exit.

