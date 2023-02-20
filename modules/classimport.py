import uiautomator2
import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

device = uiautomator2.connect("eqcieehmnbdqs8ws")

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

            data = pytesseract.image_to_data(img, output_type='dict')

            boxes = len(data['level'])

            for i in range(boxes):
                if data['text'][i] == text:
                    print(data['left'][i], data['top'][i], data['width'][i], data['height'][i], data['text'][i])
                    coord = int(data['left'][i]), int(data['top'][i]), int(data['width'][i]), int(data['height'][i])
                    CenterCoord = (coord[0]+(coord[2]/2), coord[1]+(coord[3]/2))
                    x, y = CenterCoord
                    device.click(x, y)
                    os.remove('asset/temp/screen.png')
#Exemple
# detect_to = Text()
# detect_to.TextMatch("TO")
