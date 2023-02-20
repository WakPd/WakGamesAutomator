import uiautomator2
from pathlib import Path

info = Path("save/device.txt")
if info.exists:
    deviceinfo = open("save/device.txt")
    info = deviceinfo.read()

d = uiautomator2.connect(info)

def tog_rung():
    d.app_start("global.ngelgames.tog","com.google.firebase.MessagingUnityPlayerActivity")