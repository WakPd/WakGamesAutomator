import uiautomator2
from pathlib import Path
from classimport import Button
from classimport import Text

info = Path("save/device.txt")
if info.exists:
    deviceinfo = open("save/device.txt")
    info = deviceinfo.read()

d = uiautomator2.connect(info)

def nikke_rung():
    d.app_start("com.proximabeta.nikke", "com.shiftup.nk.MainActivity")
    touch_to_continue = Text()
    Text.TextMatch('TO')
