from pathlib import Path
import os

file = Path("save/device.txt")
if file.exists():
    os.system('python main.py')
else:
    os.system('python devices.py')