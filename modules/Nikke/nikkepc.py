import uiautomator2
from pathlib import Path
from modules.pcclass import GameWindow
from modules.pcclass import Text
from modules.pcclass import Button
import time

def NikkeWin():
    GameWindow("NIKKE")

def nikkepc_sale():
    NikkeWin()
    shop_btn = Button
    shop_img = r'assets\Nikke\shop.png'
    shop_btn.Match(shop_img)