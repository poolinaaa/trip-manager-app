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

import customtkinter
import PIL.Image
from datetime import datetime

class FrameBase(tk.Frame):

    def __init__(self, masterWindow, colorOfBg, countryName, **kwargs):
        super().__init__(master=masterWindow, bg=colorOfBg,
                         highlightbackground=colorOfBg, highlightcolor=colorOfBg, **kwargs)
        self.countryName = countryName

    def loadFrame(self, frameToLoad):
        # Przełącz się na frame2
        if frameToLoad is not None:
            self.grid_remove()  # Ukryj aktualną ramkę
            frameToLoad.grid()