import os
import threading
import tkinter
import random
import sys
from tkinter.constants import BOTH, YES, NW

from Body.Listen import MicExecution
from OS.Windows import Lock_pc
from OS.Windows import Shutdown_pc
from OS.Windows import Screen_shot
from OS.Windows import battery_per
from Social_media.NewsRead import latestnews
from OS.Windows import Camera_photo
from Social_media.Whatsapp import sendMessage
from Body.Speak import Speak


def jarvis():
    while True:
        task_execution(MicExecution().lower())

def run():
    threading.Thread(target=jarvis).start()

    def flush(self):
        pass


def stop():
    os.system("TASKKILL /F /im python.exe") and os.system("TASKKILL /F /im Jarvis.py") and os.system(
        "TASKKILL /F /im Jarvis.exe")


def task_execution(sentences):
    keyword_dict = {"whatsapp": True,
                    "shut down": True,
                    "battery": True,
                    "screenshot": True,
                    "camera": True,
                    "news": True,
                    "lock": True,
                    "hello": True,
                    "fine": True}

    # Split the input string into individual words
    global a
    words = sentences.split()
    # Iterate through the words and check if they exist in the keyword dictionary
    for word in words:
        if word in keyword_dict:
            a = word  # If any word matches, return True

    if a == "news" in sentences:
        latestnews()

    elif a == "lock" in sentences:
        Lock_pc()

    elif a == "hello" in sentences:
        Speak("Hello sir, how's your day going")

    elif a == "fine" in sentences:
        Speak("Good to hear sir! What can i do for you today?")

    elif a == "exit" in sentences:
        print()

    elif a == "shut down" in sentences:
        Shutdown_pc()

    elif a == "battery" in sentences:
        battery_per()

    elif a == "screenshot" in sentences:
        Screen_shot()

    elif a == "camera" in sentences:
        Camera_photo()

    elif a == "whatsapp" in sentences:
        sendMessage()

    else:
        pass

screen_main = tkinter.Tk()
screen_main.title('Jarvis')
screen_main.configure(background='black', highlightbackground='blue', highlightthickness=5)
screen_main.attributes('-fullscreen', True)
screen_main.iconbitmap('GUI\\Icon\\jarvis.ico')

canvas = tkinter.Canvas(width=900, height=540, bg='black', highlightbackground='dark grey', highlightthickness=5)
canvas.pack(expand=YES, fill=BOTH)
photo = tkinter.PhotoImage(file='GUI\\jarviss.gif')
canvas.create_image(80, 5, image=photo, anchor='nw')

start_button = tkinter.Button(screen_main, background='black', fg='#0066CC', font=('Courier New bold', 40),
                              text='START', height = 1, width=7, borderwidth=0.5,
                              command=run)
start_button.place(x=1500, y=300)
stop_button = tkinter.Button(screen_main, background='black', fg='#0066CC', font=('Courier New bold', 40),
                             text='STOP', height = 1, width=7, borderwidth=0.5,
                             command=stop)
stop_button.place(x=1500, y=600)

terminal = tkinter.Text(screen_main)
terminal.configure(background='black', fg='white', highlightbackground='dark blue', highlightthickness=5)

terminal.configure(width=45, height=36.5999)
terminal.configure(font=('Bruce Forever', 15))
terminal.place(x=10, y=10)


class Redirect:
  def __init__(self, widget, autoscroll=True):
    self.widget = widget  # Store the widget for writing output
    self.autoscroll = autoscroll  # Flag for automatic scrolling

  def write(self, text):
    self.widget.insert('end', text)  # Insert text to the end of the widget
    if self.autoscroll:
      self.widget.see('end')  # Scroll to the end if autoscroll is enabled



old_stdout = sys.stdout
sys.stdout = Redirect(terminal)
screen_main.mainloop()