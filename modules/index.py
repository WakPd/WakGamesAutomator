import uiautomator2
from devices import dinfo

info = dinfo.get()
print(info)
d = uiautomator2.connect(info)

def nikke_rung():
    d.app_start("com.proximabeta.nikke", "com.shiftup.nk.MainActivity")
def tog_rung():
    d.app_start("global.ngelgames.tog","com.google.firebase.MessagingUnityPlayerActivity")

