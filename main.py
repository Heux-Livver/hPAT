from win32api import *
from win32gui import *
from win32con import *
from win32ui import *
from random import *
from tkinter import *
from random import *
import tkinter as tk
import time

def PatBltF():
    x = GetSystemMetrics(0)
    y = GetSystemMetrics(1)
    desk = GetDC(0)

    for i in range(1, 2000):
        brush = CreateSolidBrush(RGB(
            randrange(255),
            randrange(255),
            randrange(255)
        ))
        SelectObject(desk, brush)
        PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
        DeleteObject(brush)

PatBltF()

time.sleep(10)

root = tk.Tk()
root.attributes("-fullscreen", True)
root.overrideredirect(1)

label = tk.Label(root, text="LOL TRY ???+???(ONLY ONE COMBINATION WORKS)!", width=50, height=50)
label.pack()
root.protocol("WM_DELETE_WINDOW", PatBltF)
root.mainloop()

