import customtkinter
import os
import os.path
import time
import main

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

devroot = customtkinter.CTk()
devroot.geometry("500x300")
devroot.title("Device")
devroot.iconbitmap(default="assets\icon.ico")

dinfo = customtkinter.StringVar()
def device():
    devroot.destroy()
    os.system("python main.py")

frame = customtkinter.CTkFrame(master = devroot)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

label = customtkinter.CTkLabel(master = frame, text = "Device Info", text_color = "blue", font = ("Routtage", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master = frame, textvariable = dinfo, placeholder_text = "Device ID")
entry1.pack(pady = 12, padx = 10)


button = customtkinter.CTkButton(master = frame, text = "Submit", command = device)
button.pack(pady = 12, padx = 10)


devroot.mainloop()