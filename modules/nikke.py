import uiautomator2
from pathlib import Path
from modules.classimport import Button
from modules.classimport import Text
import time


info = Path("save/device.txt")
if info.exists:
    deviceinfo = open("save/device.txt")
    info = deviceinfo.read()

device = uiautomator2.connect(info)

def nikke_lobby():
    lobby_txt = Text
    lobby_txt.TextMatch('Lobby')

def nikke_rung():
    device.app_start("com.proximabeta.nikke", "com.shiftup.nk.MainActivity")
    to_text = Text
    to_text.TextMatch('TO')
    cross_img = 'assets/Nikke/cross.png'
    cross_btn = Button
    cross_btn.Match(cross_img)
    nikke_lobby()
    print("End of the process")

def nikke_shop():
    shop_txt = Text
    shop_txt.TextMatch('Shop')

def nikke_sale():
    nikke_shop()
    sale_btn_img = 'assets/Nikke/sale.png'
    sale_btn = Button
    sale_btn.Match(sale_btn_img)
    buy_btn_img = 'assets/Nikke/buy.png'
    buy_btn = Button
    buy_btn.Match(buy_btn_img)
    tap_to_claim_txt = Text
    tap_to_claim_txt.TextMatch('Tap')
    print("End of the process")