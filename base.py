import tkinter as tk
from tkcalendar import *
from tkinter import *
import tkinter as tk
from tkinter import *
from sqlite3 import *



class FrameBase(tk.Frame):

    def __init__(self, masterWindow, colorOfBg, countryName, baseCurrency, **kwargs):
        super().__init__(master=masterWindow, bg=colorOfBg,
                         highlightbackground=colorOfBg, highlightcolor=colorOfBg, **kwargs)
        self.countryName = countryName
        self.baseCurrency = baseCurrency

    def loadFrame(self, frameToLoad):
        
        if frameToLoad is not None:
            self.grid_remove() 
            frameToLoad.grid()