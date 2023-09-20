import tkinter.font

import tkinter as tk

from ctypes import windll

from funcBehaviorFrames import appearance
import config as c
from tkcalendar import *

from tkinter import *
from sqlite3 import *


from frame1 import Frame1
from frame2 import Frame2
from frame3 import Frame3
from frame4 import Frame4


class FrameBase(tk.Frame):

    def __init__(self, masterWindow, colorOfBg, countryName, **kwargs):
        super().__init__(master=masterWindow, bg=colorOfBg,
                         highlightbackground=colorOfBg, highlightcolor=colorOfBg, **kwargs)
        self.countryName = countryName

    def loadFrame(self, frameToLoad):

        if frameToLoad is not None:
            self.grid_remove()
            frameToLoad.grid()


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('WanderWisely')
        self.geometry("918x700")
        self.minsize(918, 700)
        self.maxsize(918, 700)
        self.bgColor = '#295873'
        self.highlight = '#1c3c4f'
        self.details = '#162f3d'
        self.configure(background=self.bgColor)
        self.countryName = tk.StringVar(value='your country')
        self.baseCurrency = tk.StringVar(value='your base currency')
        c.dateStart = tk.StringVar()
        c.dateEnd = tk.StringVar()

        c.titleFont = tkinter.font.Font(family="Lato", size=13, weight="bold")
        c.questionFont = tkinter.font.Font(
            family="Lato", size=11, weight="bold")
        
        self.start()
        appearance()

    def start(self):
        self.frame1 = Frame1(self, self.bgColor, self.countryName, self.baseCurrency)
        self.frame2 = Frame2(self, self.bgColor, self.frame1, self.countryName, self.baseCurrency)
        self.frame3 = Frame3(self, self.bgColor, self.frame1, self.countryName, self.baseCurrency)
        self.frame4 = Frame4(self, self.bgColor, self.frame1, self.countryName, self.baseCurrency)

        self.frame1.setFrames(self.frame1, self.frame2,
                              self.frame3, self.frame4)

        for frame in (self.frame1, self.frame2, self.frame3, self.frame4):

            frame.grid(row=0, column=0, sticky='nsew')

        self.frame1.grid(row=0, column=0, sticky='nsew')
        self.frame2.grid_remove()
        self.frame3.grid_remove()
        self.frame4.grid_remove()

    def clearView(self):
        self.frame1.grid_remove()
        self.frame2.grid_remove()
        self.frame3.grid_remove()
        self.frame4.grid_remove()


windll.shcore.SetProcessDpiAwareness(1)


app = Window()

app.mainloop()
