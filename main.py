import customtkinter
from PIL import Image, ImageTk
import pyperclip
import os
from pathlib import Path
from devices import dinfo
from modules.index import tog_rung, nikke_rung


customtkinter.set_appearance_mode("system")

root = customtkinter.CTk();
root.title("Games Automator")
root.geometry("500x450")

root.columnconfigure(0, weight = 1)

#All external implementations


Nikkelogo = customtkinter.CTkImage(light_image = Image.open(r"assets\nikke.png"), size = (40,40))
Toglogo = customtkinter.CTkImage(light_image=Image.open(r"assets\tog.jpg"), size = (40,40)) 

#function
def cpy_id():
    pyperclip.copy(dinfo.get())


def nikke():
    if Nikke_run._check_state is True:
        nikke_rung()

def tog():
    if tog_run._check_state is True:
        tog_rung()

#Menu
Menu = customtkinter.CTkTabview(master = root, height = 300)
Menu.grid(sticky = "NS")

#Device Info
device = customtkinter.CTkTabview(master = root, height = 80)
device.grid(sticky = "NS")

device.add("Device Info")

device_lbl = customtkinter.CTkLabel(master = device.tab("Device Info"), text = dinfo.get())
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

Nikke_valid = customtkinter.CTkButton(master = Menu.tab("Nikke"), text = "Start", command=nikke)
Nikke_valid.grid(padx = 50)

#TOG
Menu.add("TOG:M Great Journey")

tog_lbl1 = customtkinter.CTkLabel(master = Menu.tab("TOG:M Great Journey"), text = "You choose the Game TOG:M Great Journey")
tog_lbl1.grid(padx = 50)

tog_logo = customtkinter.CTkLabel(master = Menu.tab("TOG:M Great Journey"), image = Toglogo, text="")
tog_logo.grid(padx = 50)

tog_lbl2 = customtkinter.CTkLabel(master = Menu.tab("TOG:M Great Journey"), text = "Here are the differents options :")
tog_lbl2.grid(padx = 50)

tog_run = customtkinter.CTkCheckBox(master = Menu.tab("TOG:M Great Journey"), text = "Run The Game", onvalue=1, offvalue=0)
tog_run.grid(padx = 50, pady = 10)

tog_valid = customtkinter.CTkButton(master = Menu.tab("TOG:M Great Journey"), text = "Start", command=tog)
tog_valid.grid(padx = 50)
