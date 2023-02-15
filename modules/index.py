import uiautomator2
from pathlib import Path

info = Path("save/device.txt")
if info.exists:
    deviceinfo = open("save/device.txt")
    info = deviceinfo.read()

d = uiautomator2.connect(info)

def nikke_rung():
    d.app_start("com.proximabeta.nikke", "com.shiftup.nk.MainActivity")
def tog_rung():
    d.app_start("global.ngelgames.tog","com.google.firebase.MessagingUnityPlayerActivity")

