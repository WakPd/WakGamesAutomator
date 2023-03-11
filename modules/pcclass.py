import pyautogui
import cv2
import pytesseract
import os

def GameWindow(gamewindowname):
    import win32gui
    hwnd = win32gui.FindWindowEx(0,0,0, gamewindowname)
    win32gui.SetForegroundWindow(hwnd)

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

class Button:
    @staticmethod
    def Match(object):
            
            base = pyautogui.screenshot()
            base.save('assets/temp/screen_btn.png')
            base = r'assets/temp/screen_btn.png'

            img = cv2.imread(base)
            tmplt =  cv2.imread(object)

            hh, ww = tmplt.shape[:2]

            tmplt_mask = tmplt[:,:,2]
            tmplt_mask = cv2.merge([tmplt_mask,tmplt_mask,tmplt_mask])

            tmplt2 = tmplt[:,:,0:3]
            corrimg = cv2.matchTemplate(img,tmplt2,cv2.TM_CCORR_NORMED, mask=tmplt_mask)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(corrimg)
            max_val_ncc = '{:.3f}'.format(max_val)

            print("correlation match score: " + max_val_ncc)
            xx = max_loc[0]
            yy = max_loc[1]

            print('Find at ', xx, yy)
            pyautogui.click(xx, yy)
            os.remove('assets/temp/screen_btn.png')



#Text Dectection and text clicker
class Text:
      @staticmethod
      def TextMatch(text):
            
            base = pyautogui.screenshot()
            base.save('assets/temp/screen_txt.png')
            base = r'assets/temp/screen_txt.png'
            img = cv2.imread(base)

            test = pytesseract.image_to_data(img, output_type='dict')
                
            if text in test['text']:
                print(text, ' Find')
            else:
                while text not in test['text']:
                    os.remove('assets/temp/screen_txt.png')
                    base = pyautogui.screenshot()
                    base.save('assets/temp/screen_txt.png')
                    base = r'assets/temp/screen_txt.png'
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
                    pyautogui.click(x, y)
            os.remove('assets/temp/screen_txt.png')
#Exemple
# detect_to = Text()
# detect_to.TextMatch("TO")
