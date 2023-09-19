import tkinter.font
import requests
import json
import tkinter as tk
from currencyFunc import checkingCurrency, checkingBase
from ctypes import windll
from partialForms import ThemeSection
from funcBehaviorFrames import counterFrame1, appearance, confirmButton, submitDepartureDate, clearEntry, multipleFuncButton, savingLandmarks, AttractionToSee
import config as c
from funcPlots import createPlotButton, createPlotButtonAll, createPlotButtonLastMonth
from plotsWeather import createPlotWeatherCurrent, createPlotWeatherYearAgo
from tkcalendar import *
import customtkinter
from tkinter import *
from PIL import ImageTk
import datetime
import config as c
import requests
import json
import tkinter as tk
from tkinter import *
from sqlite3 import *
import csv
from geoFunc import getDistanceBetweenPoints, searchAttractions
import webbrowser
import customtkinter
import PIL.Image
from datetime import datetime
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
        c.baseCurrency = tk.StringVar(value='your base currency')
        c.dateStart = tk.StringVar()
        c.dateEnd = tk.StringVar()

        c.titleFont = tkinter.font.Font(family="Lato", size=13, weight="bold")
        c.questionFont = tkinter.font.Font(
            family="Lato", size=11, weight="bold")
        c.errorFont = tkinter.font.Font(family="Lato", size=9, weight="bold")
        self.start()
        appearance()

    def start(self):
        self.frame1 = Frame1(self, self.bgColor, self.countryName)
        self.frame2 = Frame2(self, self.bgColor, self.frame1, self.countryName)
        self.frame3 = Frame3(self, self.bgColor, self.frame1, self.countryName)
        self.frame4 = Frame4(self, self.bgColor, self.frame1, self.countryName)

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
