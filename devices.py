import customtkinter
import os
import os.path
import time

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x300")
root.title("Device")

frame = customtkinter.CTkFrame(master = root)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

label = customtkinter.CTkLabel(master = frame, text = "Device Info", text_color = "blue", font = ("Routtage", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master = frame, placeholder_text = "Device ID")
entry1.pack(pady = 12, padx = 10)

def device():
    directory = 'save'
    filename = "device.txt"
    file_path = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    file = open(file_path, "w")
    file.write(entry1.get())
    file.close()   
    root.destroy()
    os.system('python main.py')


button = customtkinter.CTkButton(master = frame, text = "Submit", command = device)
button.pack(pady = 12, padx = 10)




root.mainloop()