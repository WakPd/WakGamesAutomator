import uiautomator2
import cv2
import pytesseract
import os
import time
from pathlib import Path

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

info = Path("save/device.txt")
if info.exists:
    deviceinfo = open("save/device.txt")
    info = deviceinfo.read()
device = uiautomator2.connect(info)

#Button Maker and matcher
class Button:
    @staticmethod
    def Match(object):
            
            base = device.screenshot('assets/temp/screen_btn.png')

            img = cv2.imread(base)
            tmplt =  cv2.imread(object)

            hh, ww = tmplt.shape[:2]

            corrimg = cv2.matchTemplate(img, tmplt, cv2.TM_CCORR_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(corrimg)
            max_val_ncc = '{:.3}'.format(max_val)
            print("correlation match score: " + max_val_ncc)

            xx = max_loc[0]
            yy = max_loc[1]
            print('xmatch =',xx,'ymatch =',yy)

            coord = int(xx), int(yy), int(xx+ww), int(yy+hh)
            CenterCoord = (coord[0]+(coord[2]/2), coord[1]+(coord[3]/2))
            x, y = CenterCoord
            print('Find at ', x, y)
            device.click(x, y)
            os.remove('assets/temp/screen_btn.png')



#Text Dectection and text clicker
class Text:
      @staticmethod
      def TextMatch(text):
            
            base = device.screenshot('assets/temp/screen_txt.png')
            img = cv2.imread(base)

            test = pytesseract.image_to_data(img, output_type='dict')
                
            if text in test['text']:
                print(text, ' Find')
            else:
                while text not in test['text']:
                    os.remove('assets/temp/screen_txt.png')
                    base = device.screenshot('assets/temp/screen_txt.png')
                    img = cv2.imread(base)
                    test = pytesseract.image_to_data(img, output_type='dict')
                print(text, ' Find')
                
            img = cv2.imread('assets/temp/screen_txt.png')
            data = pytesseract.image_to_data(img, output_type='dict')

            boxes = len(data['level'])

            for i in range(boxes):
                if data['text'][i] == text:
                    coord = int(data['left'][i]), int(data['top'][i]), int(data['width'][i]), int(data['height'][i])
                    CenterCoord = (coord[0]+(coord[2]/2), coord[1]+(coord[3]/2))
                    x, y = CenterCoord
                    print(text, ' find at ', x, y)
                    device.click(x, y)
            os.remove('assets/temp/screen_txt.png')
#Exemple
# detect_to = Text()
# detect_to.TextMatch("TO")
