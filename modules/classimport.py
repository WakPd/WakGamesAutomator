import uiautomator2
import cv2
import pytesseract
import os
import time
from pathlib import Path

pytesseract.pytesseract.tesseract_cmd = "Tesseract-OCR\\tesseract.exe"
info = Path("save/device.txt")
if info.exists:
    deviceinfo = open("save/device.txt")
    info = deviceinfo.read()
device = uiautomator2.connect("info")

#Button Maker and matcher
class Button:
    @staticmethod
    def Match(object):
            device.image.match(object)
            device.image.click(object)
#check GitHub UIautomator for how to use

#Text Dectection and text clicker
class Text:
      @staticmethod
      def TextMatch(text):
            
            base = device.screenshot('assets/temp/screen.png')
            img = cv2.imread(base)

            test = pytesseract.image_to_data(img, output_type='dict')
                
            if text in test['text']:
                print(text, ' Find')
            else:
                while text not in test['text']:
                    print("0")
                    os.remove('assets/temp/screen.png')
                    base = device.screenshot('assets/temp/screen.png')
                    img = cv2.imread(base)
                    test = pytesseract.image_to_data(img, output_type='dict')
                print(text, ' Find')
                
            img = cv2.imread('assets/temp/screen.png')
            data = pytesseract.image_to_data(img, output_type='dict')

            boxes = len(data['level'])

            for i in range(boxes):
                if data['text'][i] == text:
                    print(data['left'][i], data['top'][i], data['width'][i], data['height'][i], data['text'][i])
                    coord = int(data['left'][i]), int(data['top'][i]), int(data['width'][i]), int(data['height'][i])
                    CenterCoord = (coord[0]+(coord[2]/2), coord[1]+(coord[3]/2))
                    x, y = CenterCoord
                    print(text, ' find at ', x, y)
                    device.click(x, y)
            os.remove('assets/temp/screen.png')
#Exemple
# detect_to = Text()
# detect_to.TextMatch("TO")
