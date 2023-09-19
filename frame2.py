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
from base import FrameBase

class Frame2(FrameBase):

    def __init__(self, masterWindow, colorOfBg, frame1, countryName):
        super().__init__(masterWindow=masterWindow,
                         colorOfBg=colorOfBg, countryName=countryName)

        self.frame1 = frame1
        self.load()

    def load(self):
        self.tkraise()

        self.backButton = customtkinter.CTkButton(master=self, text='BACK', fg_color=c.details, width=40, height=40,
                                                  command=lambda: multipleFuncButton(clearEntry(self.entryStart, self.entryEnd), self.loadFrame(self.frame1)))
        self.backButton.pack(side=TOP, anchor=NW)

        self.labelTitle = tk.Label(master=self, text="Analyse currency rate",
                                   font=c.titleFont, bg=c.highlight, fg='white')
        self.labelTitle.pack()

        self.frameEnteringDate = tk.Frame(
            master=self, bg=c.highlight, highlightbackground=c.bgColor, highlightcolor=c.bgColor)
        self.frameEnteringDate.pack(pady=20)

        self.labelStartDate = tk.Label(master=self.frameEnteringDate,
                                       text='Enter the start date: ', fg='white', bg=c.highlight)
        self.labelStartDate.grid(column=0, row=0)

        self.labelEndDate = tk.Label(master=self.frameEnteringDate,
                                     text='Enter the end date: ', fg='white', bg=c.highlight)
        self.labelEndDate.grid(column=1, row=0)

        self.buttonConfirmDate = customtkinter.CTkButton(master=self.frameEnteringDate, width=20, text='CONFIRM TIME SPAN', fg_color=c.details,
                                                         command=lambda: confirmButton(self, c.dateStart, c.dateEnd, baseCurrName, codeCurrency, self.fake1, self.fake2, self.fake3, self.buttonPlot1, self.buttonPlot2, self.buttonPlot3))
        self.buttonConfirmDate.grid(column=3, row=1, padx=10, pady=5)

        self.entryStart = tk.Entry(master=self.frameEnteringDate,
                                   width=28, textvariable=c.dateStart)
        self.entryStart.insert(0, 'YYYY-MM-DD')
        self.entryStart.grid(column=0, row=1, padx=5, pady=5)

        self.entryEnd = tk.Entry(master=self.frameEnteringDate,
                                 width=28, textvariable=c.dateEnd)

        self.entryEnd.insert(0, 'YYYY-MM-DD')
        self.entryEnd.grid(column=1, row=1, padx=5, pady=5)

        self.framePlots = tk.Frame(master=self, bg=c.bgColor,
                                   highlightbackground=c.bgColor, highlightcolor=c.bgColor)

        self.fake1 = customtkinter.CTkButton(
            master=self.framePlots, width=20, state=DISABLED, text='SHOW PLOT 1', fg_color=c.details)
        self.fake2 = customtkinter.CTkButton(
            master=self.framePlots, width=20, state=DISABLED, text='SHOW PLOT 2', fg_color=c.details)
        self.fake3 = customtkinter.CTkButton(
            master=self.framePlots, width=20, state=DISABLED, text='SHOW PLOT 3', fg_color=c.details)
        self.fake1.grid(column=0, row=1, padx=15, pady=10)
        self.fake2.grid(column=1, row=1, padx=15, pady=10)
        self.fake3.grid(column=2, row=1, padx=15, pady=10)

        img = (PIL.Image.open("money.png"))

        resized_image = img.resize((400, 400))
        new_image = ImageTk.PhotoImage(resized_image)

        self.pictureWidget = tk.Label(
            master=self.framePlots, image=new_image, width=400, height=400, bg=c.bgColor)

        self.pictureWidget.image = new_image
        self.pictureWidget.grid(column=0, row=2, columnspan=3, pady=10)

        self.labelPlot1 = tk.Label(
            master=self.framePlots, text='Comparison to the current rate', bg=c.bgColor, fg='white')
        self.labelPlot1.grid(column=0, row=0, padx=15)

        self.buttonPlot1 = customtkinter.CTkButton(master=self.framePlots, width=20, text='SHOW PLOT 1', fg_color=c.details,
                                                   command=lambda: createPlotButton(c.dates, c.rate, c.current, self.framePlots))

        self.labelPlot2 = tk.Label(
            master=self.framePlots, text='Rate compared to changes \nin EUR, USD, PLN, GBP', bg=c.bgColor, fg='white')
        self.labelPlot2.grid(column=1, row=0, padx=15)

        self.buttonPlot2 = customtkinter.CTkButton(master=self.framePlots, width=20, text='SHOW PLOT 2', fg_color=c.details, command=lambda: createPlotButtonAll(
            c.dates, self.framePlots, c.rate, c.eur, c.usd, c.pln, c.cny, codeCurrency))

        self.labelPlot3 = tk.Label(
            master=self.framePlots, text='Currency rate for the last 30 days', bg=c.bgColor,  fg='white')
        self.labelPlot3.grid(column=2, row=0, padx=15)

        self.buttonPlot3 = customtkinter.CTkButton(master=self.framePlots, width=20, text='SHOW PLOT 3', fg_color=c.details,
                                                   command=lambda: createPlotButtonLastMonth(baseCurrName, codeCurrency, self.framePlots))

        self.framePlots.pack()