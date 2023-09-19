
import tkinter as tk


from funcBehaviorFrames import counterFrame1, appearance, confirmButton, submitDepartureDate, clearEntry, multipleFuncButton, savingLandmarks, AttractionToSee
import config as c

from plotsWeather import createPlotWeatherCurrent, PlotYearAgo
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

class Frame4(FrameBase):

    def __init__(self, masterWindow, colorOfBg, frame1, countryName):
        super().__init__(masterWindow=masterWindow,
                         colorOfBg=colorOfBg, countryName=countryName)

        self.frame1 = frame1
        self.load()

    def load(self):
        self.tkraise()

        self.backButton = customtkinter.CTkButton(master=self, text='BACK', fg_color=c.details, width=40, height=40,
                                                  command=lambda: self.loadFrame(self.frame1))
        self.backButton.grid(column=0, row=0)

        futureData = tk.StringVar()
        pastData = tk.StringVar()

        self.calDateOfDeparture = Calendar(
            master=self, selectmode='day', date_pattern='YYYY-MM-DD')
        self.calDateOfDeparture.grid(column=1, row=1, rowspan=3, padx=50)
        self.dateDeparture = tk.StringVar(value='YYYY-MM-DD')
        self.labelSelectedDate = tk.Label(
            master=self, text=f'Select date of the departure', width=30, font=c.titleFont, bg=c.highlight, fg='white')

        self.frameForecast = tk.Frame(master=self, bg=c.bgColor,
                                      highlightbackground=c.bgColor, highlightcolor=c.bgColor)

        img = (PIL.Image.open("fog.png"))

        resized_image = img.resize((300, 300))
        new_image = ImageTk.PhotoImage(resized_image)

        self.framePic = tk.Frame(master=self.frameForecast, bg=c.bgColor)

        self.pictureWidget = tk.Label(
            master=self.framePic, image=new_image, width=300, height=300, bg=c.bgColor)

        self.pictureWidget.image = new_image
        self.pictureWidget.pack(pady=10)
        self.framePic.grid(column=0, row=1, columnspan=2)

        self.buttonFake1 = customtkinter.CTkButton(
            master=self.frameForecast, text='YEAR AGO', fg_color=c.details, state=tk.DISABLED)
        self.buttonFake2 = customtkinter.CTkButton(
            master=self.frameForecast, text='NEXT WEEK', fg_color=c.details, state=tk.DISABLED)
        self.buttonFake2.grid(column=0, row=0, sticky='w')
        self.buttonFake1.grid(column=1, row=0, sticky='w')

        self.buttonYearAgo = customtkinter.CTkButton(
            master=self.frameForecast, text='YEAR AGO', fg_color=c.details, command=lambda: PlotYearAgo(self.countryName, c.dateFlight).createPlotWeatherYearAgo(self.frameForecast, pastData, self.pictureWidget))
        self.buttonFuture = customtkinter.CTkButton(
            master=self.frameForecast, text='NEXT WEEK', fg_color=c.details,  command=lambda: createPlotWeatherCurrent(self.frameForecast, futureData, self.pictureWidget))

        self.labelTitle = tk.Label(master=self, text="Check the weather",
                                   font=c.titleFont, bg=c.highlight, fg='white')
        self.labelTitle.grid(
            column=2, row=1, columnspan=3, padx=30, sticky='w')

        self.buttonDateOfDeparture = customtkinter.CTkButton(master=self, text='SUBMIT DATE', fg_color=c.details, command=lambda: submitDepartureDate(
            self.dateDeparture, self.calDateOfDeparture, self.labelSelectedDate, self.buttonFuture, self.buttonYearAgo, self.buttonFake2, self.buttonFake1))
        self.buttonDateOfDeparture.grid(
            column=2, row=2, columnspan=3, padx=30, sticky='w')

        self.labelSelectedDate.grid(
            column=2, row=3, columnspan=3, padx=30, sticky='w')

        self.frameForecast.grid(row=4, column=0, columnspan=5, pady=15)