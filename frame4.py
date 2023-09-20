import tkinter.font
import tkinter as tk

import config as c
from plotsWeather import PlotNextWeek, PlotYearAgo
from tkcalendar import *
import customtkinter
from tkinter import *
from PIL import ImageTk
import config as c
import tkinter as tk
from tkinter import *
from sqlite3 import *
import customtkinter
import PIL.Image
from base import FrameBase


class Frame4(FrameBase):

    def __init__(self, masterWindow, colorOfBg, colorDetails, colorHighlight, frame1, countryName, baseCurrency):
        super().__init__(masterWindow=masterWindow,
                         colorOfBg=colorOfBg, colorDetails=colorDetails, colorHighlight=colorHighlight, countryName=countryName, baseCurrency=baseCurrency)

        self.frame1 = frame1
        self.colorOfBg = colorOfBg
        self.load()

    def load(self):
        self.tkraise()

        self.backButton = customtkinter.CTkButton(master=self, text='BACK', fg_color=self.colorDetails, width=40, height=40,
                                                  command=lambda: self.loadFrame(self.frame1))
        self.backButton.grid(column=0, row=0)

        futureData = tk.StringVar()
        pastData = tk.StringVar()

        self.calDateOfDeparture = Calendar(
            master=self, selectmode='day', date_pattern='YYYY-MM-DD')
        self.calDateOfDeparture.grid(column=1, row=1, rowspan=3, padx=50)
        self.dateDeparture = tk.StringVar(value='YYYY-MM-DD')
        self.labelSelectedDate = tk.Label(
            master=self, text=f'Select date of the departure', width=30, font=tkinter.font.Font(**self.titleFont), bg=self.colorHighlight, fg='white')

        self.frameForecast = tk.Frame(master=self, bg=self.colorOfBg,
                                      highlightbackground=self.colorOfBg, highlightcolor=self.colorOfBg)

        img = (PIL.Image.open("fog.png"))

        resized_image = img.resize((300, 300))
        new_image = ImageTk.PhotoImage(resized_image)

        self.framePic = tk.Frame(master=self.frameForecast, bg=self.colorOfBg)

        self.pictureWidget = tk.Label(
            master=self.framePic, image=new_image, width=300, height=300, bg=self.colorOfBg)

        self.pictureWidget.image = new_image
        self.pictureWidget.pack(pady=10)
        self.framePic.grid(column=0, row=1, columnspan=2)

        self.buttonFake1 = customtkinter.CTkButton(
            master=self.frameForecast, text='YEAR AGO', fg_color=self.colorDetails, state=tk.DISABLED)
        self.buttonFake2 = customtkinter.CTkButton(
            master=self.frameForecast, text='NEXT WEEK', fg_color=self.colorDetails, state=tk.DISABLED)
        self.buttonFake2.grid(column=0, row=0, sticky='w')
        self.buttonFake1.grid(column=1, row=0, sticky='w')

        self.buttonYearAgo = customtkinter.CTkButton(
            master=self.frameForecast, text='YEAR AGO', fg_color=self.colorDetails, command=lambda: PlotYearAgo(self.countryName, self.dateDeparture).createPlotWeatherYearAgo(self.frameForecast, pastData, self.pictureWidget))
        self.buttonFuture = customtkinter.CTkButton(
            master=self.frameForecast, text='NEXT WEEK', fg_color=self.colorDetails,  command=lambda: PlotNextWeek(self.countryName).createPlotWeatherCurrent(self.frameForecast, futureData, self.pictureWidget))

        self.labelTitle = tk.Label(master=self, text="Check the weather",
                                   font=tkinter.font.Font(**self.titleFont), bg=self.colorHighlight, fg='white')
        self.labelTitle.grid(
            column=2, row=1, columnspan=3, padx=30, sticky='w')

        self.buttonDateOfDeparture = customtkinter.CTkButton(master=self, text='SUBMIT DATE', fg_color=self.colorDetails, command=self.submitDepartureDate)
        self.buttonDateOfDeparture.grid(
            column=2, row=2, columnspan=3, padx=30, sticky='w')

        self.labelSelectedDate.grid(
            column=2, row=3, columnspan=3, padx=30, sticky='w')

        self.frameForecast.grid(row=4, column=0, columnspan=5, pady=15)

    def submitDepartureDate(self):
        self.buttonFake1.destroy()
        self.buttonFake2.destroy()
        self.dateDeparture = self.calDateOfDeparture.get_date()
        self.labelSelectedDate['text'] = f'Selected date of departure: {self.dateDeparture}'
        self.buttonFuture.grid(column=0, row=0, sticky='e')
        self.buttonYearAgo.grid(column=1, row=0, sticky='w')