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

def nikke_rung():
    device.app_start("com.proximabeta.nikke", "com.shiftup.nk.MainActivity")
    device.implicitly_wait()
    time.sleep(45)
    to_text = Text
    to_text.TextMatch('TO')
    print('Game run to the lobby screen')