import customtkinter
from PIL import Image, ImageTk
import pyperclip
import os
from pathlib import Path
from modules.nikke import *

customtkinter.set_appearance_mode("system")

root = customtkinter.CTk();
root.title("Games Automator")
root.geometry("500x450")
root.iconbitmap(default="assets\icon.ico")
root.columnconfigure(0, weight = 1)

#All external implementations

dinfo = Path("save/device.txt")
if dinfo.exists:
    deviceinfo = open("save/device.txt")
    dinfo = deviceinfo.read()

Nikkelogo = customtkinter.CTkImage(light_image = Image.open(r"assets\Nikke\nikke.png"), size = (40,40))

#function
def cpy_id():
    pyperclip.copy(dinfo)

def nikke():
        if Nikke_run._check_state is True:
            nikke_rung()
        if Nikke_sale_buy._check_state is True:
            nikke_sale()

#Menu
Menu = customtkinter.CTkTabview(master = root, height = 300)
Menu.grid(sticky = "NS")

#Device Info
device = customtkinter.CTkTabview(master = root, height = 80)
device.grid(sticky = "NS")

device.add("Device Info")

device_lbl = customtkinter.CTkLabel(master = device.tab("Device Info"), text = dinfo)
device_lbl.grid(padx = 80, pady = 10)

device_cpy = customtkinter.CTkButton(master = device.tab("Device Info"), text = "Copy ID", command = cpy_id())
device_cpy.grid(padx = 80)

#Nikke
Menu.add("Nikke")

Nikke_lbl1 = customtkinter.CTkLabel(master = Menu.tab("Nikke"), text = "You choose the Game Nikke")
Nikke_lbl1.grid(padx = 50)

Nikke_logo = customtkinter.CTkLabel(master = Menu.tab("Nikke"), image = Nikkelogo, text="")
Nikke_logo.grid(padx = 50)

Nikke_lbl2 = customtkinter.CTkLabel(master = Menu.tab("Nikke"), text = "Here are the differents options :")
Nikke_lbl2.grid(padx = 50)

Nikke_run = customtkinter.CTkCheckBox(master = Menu.tab("Nikke"), text = "Run The Game", onvalue=1, offvalue=0)
Nikke_run.grid(padx = 50, pady = 10)

Nikke_sale_buy = customtkinter.CTkCheckBox(master = Menu.tab("Nikke"), text = "Shop 100% Sale Item", onvalue=1, offvalue=0)
Nikke_sale_buy.grid(padx = 50, pady = 10)

Nikke_valid = customtkinter.CTkButton(master = Menu.tab("Nikke"), text = "Start", command=nikke)
Nikke_valid.grid(padx = 50)

root.mainloop()