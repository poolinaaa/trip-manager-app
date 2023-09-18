import tkinter.font
import requests
import json
import tkinter as tk
from currencyFunc import checkingCurrency, checkingBase
from ctypes import windll
from partialForms import ThemeSection, InitializationFrame
from funcBehaviorFrames import counterFrame1, appearance,  confirmCountry, clearView, loadFrame, confirmButton, submitDepartureDate, clearEntry, multipleFuncButton
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

import webbrowser
import customtkinter
import PIL.Image
from datetime import datetime

'''# main frame: menu
def loadFrame1():
    def searchButton():
        countryToFind = c.countryName.get().capitalize()
        global codeCurrency, baseCurrName
        baseCurrName = c.baseCurrency.get().upper()
        codeCurrency = checkingCurrency(countryToFind).upper()
        baseCurrName = checkingBase(baseCurrName)

        if codeCurrency == 'COUNTRYERROR':
            countryError = 'You have entered wrong name of country. Please try again (check full name of country)'
            errorLabel = tk.Label(
                master=frameQuestions, text=countryError, font=c.errorFont, bg=c.bgColor, fg='white')
            errorLabel.grid(column=0, row=1, columnspan=2)
            frameQuestions.after(5000, errorLabel.destroy)
        else:
            frameCurrency.title['text'] = f'Analyse changes in {codeCurrency}'
            fake1.destroy()
            fake2.destroy()
            fake3.destroy()
            buttonLoadFrame2.pack(side=tk.BOTTOM)

            buttonLoadFrame3.pack(side=tk.BOTTOM)

            buttonLoadFrame4.pack(side=tk.BOTTOM)

            if 'baseCurrName' in globals():
                params = {'base': baseCurrName, 'symbols': codeCurrency}
                r = requests.get(
                    'https://api.exchangerate.host/latest/', params)
                try:
                    data = r.json()
                except json.JSONDecodeError:
                    print('Wrong format of data.')
                else:
                    c.current = data["rates"][codeCurrency]
                    labelCurrentRate['text'] = f'Current rate: {c.current} {baseCurrName}'

    frame1.tkraise()

    nr = next(gen)

    # title
    labelTitle = tk.Label(master=frame1, text="Let's prepare for your trip!",
                          font=c.titleFont, bg=c.bgColor, fg='white')

    # fields to enter destination and base currency
    frameQuestions = tk.Frame(master=frame1, width=100,  bg=c.bgColor,
                              highlightbackground=c.bgColor, highlightcolor=c.bgColor)

    labelCountry = tk.Label(master=frameQuestions, text="What country is your destination?",
                            width=30, font=c.questionFont, bg=c.bgColor, fg='white', anchor="w")
    labelCountry.grid(column=0, row=0, pady=10)

    entryCountry = tk.Entry(master=frameQuestions,
                            width=20, textvariable=c.countryName)
    entryCountry.grid(column=1, row=0, pady=10, padx=5)

    labelBaseCurrency = tk.Label(master=frameQuestions, text="What is your base currency?",
                                 width=30, font=c.questionFont, bg=c.bgColor, fg='white', anchor="w")
    labelBaseCurrency.grid(column=0, row=2, pady=10)

    entryCurrency = tk.Entry(master=frameQuestions,
                             width=20, textvariable=c.baseCurrency)
    entryCurrency.grid(column=1, row=2, pady=10, padx=5)

    frameSections = tk.Frame(master=frame1, width=300, bg=c.bgColor,
                             highlightbackground=c.bgColor, highlightcolor=c.bgColor)

    frameCurrency = ThemeSection(frameSections, 100, 300)
    frameCurrency.addTitleLabel(title='Changes in currency')
    frameCurrency.grid(column=0, row=0, sticky='nsew')
    frameCurrency.addImage('cash.png')

    labelCurrentRate = tk.Label(
        master=frameCurrency, text='Current rate:', bg=c.highlight, font=c.errorFont, fg='white')

    # flights
    frameFlights = ThemeSection(frameSections, 100, 300)

    frameFlights.addTitleLabel(title='Geographical details')
    frameFlights.grid(column=1, row=0, sticky='nsew')
    frameFlights.addImage('plane.png')

    # weather
    frameWeather = ThemeSection(frameSections, 100, 300)
    frameWeather.addTitleLabel(title='Check the weather')
    frameWeather.grid(column=2, row=0, sticky='nsew')
    frameWeather.addImage('sun.png')

    fake1 = customtkinter.CTkButton(master=frameCurrency, text='CURRENCY', fg_color=c.details,
                                    width=20, state=tk.DISABLED)
    fake2 = customtkinter.CTkButton(master=frameFlights, text='GEOGRAPHY', fg_color=c.details,
                                    width=20, state=tk.DISABLED)
    fake3 = customtkinter.CTkButton(master=frameWeather, text='WEATHER', fg_color=c.details,
                                    width=20, state=tk.DISABLED)

    buttonLoadFrame2 = customtkinter.CTkButton(master=frameCurrency, text='CURRENCY', fg_color=c.details,
                                               width=20, command=lambda: loadFrame(frame1, loadFrame2))
    buttonLoadFrame3 = customtkinter.CTkButton(master=frameFlights, text='GEOGRAPHY', fg_color=c.details,
                                               width=20, command=lambda: loadFrame(frame1, loadFrame3))
    buttonCountrySearch = customtkinter.CTkButton(
        master=frameQuestions, width=8, fg_color=c.highlight, text="SEARCH", command=searchButton)
    buttonLoadFrame4 = customtkinter.CTkButton(master=frameWeather, text='WEATHER', fg_color=c.details,
                                               width=20, command=lambda: loadFrame(frame1, loadFrame4))
    buttonCountrySearch.grid(column=0, row=3, columnspan=2, pady=10)

    for widget in (labelTitle, frameQuestions, labelCurrentRate, frameSections):
        widget.pack()

    if nr == 1:
        fake1.pack(side=tk.BOTTOM)
        fake2.pack(side=tk.BOTTOM)
        fake3.pack(side=tk.BOTTOM)
    else:
        buttonLoadFrame2.pack(side=tk.BOTTOM)
        buttonLoadFrame3.pack(side=tk.BOTTOM)
        buttonLoadFrame4.pack(side=tk.BOTTOM)
    # loading buttons


# frame with currency rate


def loadFrame2():
    frame2.tkraise()

    backButton = customtkinter.CTkButton(master=frame2, text='BACK', fg_color=c.details, width=40, height=40,
                                         command=lambda: multipleFuncButton(clearEntry(entryStart, entryEnd), loadFrame(frame2, loadFrame1)))
    backButton.pack(side=TOP, anchor=NW)

    labelTitle = tk.Label(master=frame2, text="Analyse currency rate",
                          font=c.titleFont, bg=c.highlight, fg='white')
    labelTitle.pack()

    frameEnteringDate = tk.Frame(
        master=frame2, bg=c.highlight, highlightbackground=c.bgColor, highlightcolor=c.bgColor)
    frameEnteringDate.pack(pady=20)

    labelStartDate = tk.Label(master=frameEnteringDate,
                              text='Enter the start date: ', fg='white', bg=c.highlight)
    labelStartDate.grid(column=0, row=0)

    labelEndDate = tk.Label(master=frameEnteringDate,
                            text='Enter the end date: ', fg='white', bg=c.highlight)
    labelEndDate.grid(column=1, row=0)

    buttonConfirmDate = customtkinter.CTkButton(master=frameEnteringDate, width=20, text='CONFIRM TIME SPAN', fg_color=c.details,
                                                command=lambda: confirmButton(frame2, c.dateStart, c.dateEnd, baseCurrName, codeCurrency, fake1, fake2, fake3, buttonPlot1, buttonPlot2, buttonPlot3))
    buttonConfirmDate.grid(column=3, row=1, padx=10, pady=5)

    entryStart = tk.Entry(master=frameEnteringDate,
                          width=28, textvariable=c.dateStart)
    entryStart.insert(0, 'YYYY-MM-DD')
    entryStart.grid(column=0, row=1, padx=5, pady=5)

    entryEnd = tk.Entry(master=frameEnteringDate,
                        width=28, textvariable=c.dateEnd)

    entryEnd.insert(0, 'YYYY-MM-DD')
    entryEnd.grid(column=1, row=1, padx=5, pady=5)

    framePlots = tk.Frame(master=frame2, bg=c.bgColor,
                          highlightbackground=c.bgColor, highlightcolor=c.bgColor)

    fake1 = customtkinter.CTkButton(
        master=framePlots, width=20, state=DISABLED, text='SHOW PLOT 1', fg_color=c.details)
    fake2 = customtkinter.CTkButton(
        master=framePlots, width=20, state=DISABLED, text='SHOW PLOT 2', fg_color=c.details)
    fake3 = customtkinter.CTkButton(
        master=framePlots, width=20, state=DISABLED, text='SHOW PLOT 3', fg_color=c.details)
    fake1.grid(column=0, row=1, padx=15, pady=10)
    fake2.grid(column=1, row=1, padx=15, pady=10)
    fake3.grid(column=2, row=1, padx=15, pady=10)

    img = (Image.open("money.png"))

    resized_image = img.resize((400, 400))
    new_image = ImageTk.PhotoImage(resized_image)

    pictureWidget = tk.Label(
        master=framePlots, image=new_image, width=400, height=400, bg=c.bgColor)

    pictureWidget.image = new_image
    pictureWidget.grid(column=0, row=2, columnspan=3, pady=10)

    labelPlot1 = tk.Label(
        master=framePlots, text='Comparison to the current rate', bg=c.bgColor, fg='white')
    labelPlot1.grid(column=0, row=0, padx=15)

    buttonPlot1 = customtkinter.CTkButton(master=framePlots, width=20, text='SHOW PLOT 1', fg_color=c.details,
                                          command=lambda: createPlotButton(c.dates, c.rate, c.current, framePlots))

    labelPlot2 = tk.Label(
        master=framePlots, text='Rate compared to changes \nin EUR, USD, PLN, GBP', bg=c.bgColor, fg='white')
    labelPlot2.grid(column=1, row=0, padx=15)

    buttonPlot2 = customtkinter.CTkButton(master=framePlots, width=20, text='SHOW PLOT 2', fg_color=c.details, command=lambda: createPlotButtonAll(
        c.dates, framePlots, c.rate, c.eur, c.usd, c.pln, c.cny, codeCurrency))

    labelPlot3 = tk.Label(
        master=framePlots, text='Currency rate for the last 30 days', bg=c.bgColor,  fg='white')
    labelPlot3.grid(column=2, row=0, padx=15)

    buttonPlot3 = customtkinter.CTkButton(master=framePlots, width=20, text='SHOW PLOT 3', fg_color=c.details,
                                          command=lambda: createPlotButtonLastMonth(baseCurrName, codeCurrency, framePlots))

    framePlots.pack()


def loadFrame3():
    frame3.tkraise()
    frameOptions = tk.Frame(frame3, bg=c.highlight)
    backButton = customtkinter.CTkButton(master=frame3, text='BACK', fg_color=c.details, width=40, height=40,
                                         command=lambda: loadFrame(frame3, loadFrame1))
    backButton.pack(side=TOP, anchor=NW)

    labelTitle = tk.Label(master=frame3, text=f"Discover some geographical facts about {c.countryName.get().capitalize()}",
                          font=c.titleFont, bg=c.bgColor, fg='white')
    labelTitle.pack()
    frameOptions.pack()

    labelDepartureCountry = tk.Label(master=frameOptions, text="What is your departure country?",
                                     width=30, font=c.questionFont, bg=c.bgColor, fg='white', anchor="w")
    labelDepartureCountry.grid(column=0, row=0)

    departureCountry = tk.StringVar(value='country')

    entryDepartureCountry = tk.Entry(
        master=frameOptions, textvariable=departureCountry)
    entryDepartureCountry.grid(column=0, row=1)

    labelUnit = tk.Label(master=frameOptions, text='Select the unit in which the distance will be displayed',
                         font=c.questionFont, bg=c.bgColor, fg='white', anchor="w")
    labelUnit.grid(column=1, row=0, columnspan=2)

    var = tk.StringVar(value='kilometers')

    kmButton = tk.Radiobutton(
        master=frameOptions, text='kilometers', variable=var, value='kilometers', bg='#9dc0d1')
    milesButton = tk.Radiobutton(
        master=frameOptions, text='miles', variable=var, value='miles', bg='#9dc0d1')

    kmButton.grid(column=1, row=1, pady=5)
    milesButton.grid(column=2, row=1, pady=5)

    frameCities = tk.Frame(frame3, bg=c.highlight, height=450)
    frameCities.pack(side=LEFT, anchor='n', padx=55, pady=10)
    preparingLabelCities(frameCities)
    frameCheckbutton = tk.Frame(
        master=frame3, bg='#9dc0d1', width=300, height=450)

    img = (Image.open("globe.png"))

    resized_image = img.resize((300, 300))
    new_image = ImageTk.PhotoImage(resized_image)

    pictureWidget = tk.Label(
        master=frameCheckbutton, image=new_image, width=300, height=300, bg=c.bgColor)

    pictureWidget.image = new_image
    pictureWidget.pack()

    frameCheckbutton.pack(side=LEFT, pady=30, anchor='n')

    buttonConfirmCountry = customtkinter.CTkButton(master=frameOptions, text='CONFIRM COUNTRY', fg_color=c.details,
                                                   command=lambda: confirmCountry(departureCountry, frameCheckbutton, var.get()))
    buttonConfirmCountry.grid(row=2, column=0, columnspan=3, pady=20)


# frame with weather


def loadFrame4():
    frame4.tkraise()

    backButton = customtkinter.CTkButton(master=frame4, text='BACK', fg_color=c.details, width=40, height=40,
                                         command=lambda: loadFrame(frame4, loadFrame1))
    backButton.grid(column=0, row=0)

    futureData = tk.StringVar()
    pastData = tk.StringVar()

    calDateOfDeparture = Calendar(
        master=frame4, selectmode='day', date_pattern='YYYY-MM-DD')
    calDateOfDeparture.grid(column=1, row=1, rowspan=3, padx=50)
    dateDeparture = tk.StringVar(value='YYYY-MM-DD')
    labelSelectedDate = tk.Label(
        master=frame4, text=f'Select date of the departure', width=30, font=c.titleFont, bg=c.highlight, fg='white')

    frameForecast = tk.Frame(master=frame4, bg=c.bgColor,
                             highlightbackground=c.bgColor, highlightcolor=c.bgColor)

    img = (Image.open("fog.png"))

    resized_image = img.resize((300, 300))
    new_image = ImageTk.PhotoImage(resized_image)

    framePic = tk.Frame(master=frameForecast, bg=c.bgColor)

    pictureWidget = tk.Label(
        master=framePic, image=new_image, width=300, height=300, bg=c.bgColor)

    pictureWidget.image = new_image
    pictureWidget.pack(pady=10)
    framePic.grid(column=0, row=1, columnspan=2)

    buttonFake1 = customtkinter.CTkButton(
        master=frameForecast, text='YEAR AGO', fg_color=c.details, state=tk.DISABLED)
    buttonFake2 = customtkinter.CTkButton(
        master=frameForecast, text='NEXT WEEK', fg_color=c.details, state=tk.DISABLED)
    buttonFake2.grid(column=0, row=0, sticky='w')
    buttonFake1.grid(column=1, row=0, sticky='w')

    buttonYearAgo = customtkinter.CTkButton(
        master=frameForecast, text='YEAR AGO', fg_color=c.details, command=lambda: createPlotWeatherYearAgo(frameForecast, pastData, pictureWidget))
    buttonFuture = customtkinter.CTkButton(
        master=frameForecast, text='NEXT WEEK', fg_color=c.details,  command=lambda: createPlotWeatherCurrent(frameForecast, futureData, pictureWidget))

    labelTitle = tk.Label(master=frame4, text="Check the weather",
                          font=c.titleFont, bg=c.highlight, fg='white')
    labelTitle.grid(column=2, row=1, columnspan=3, padx=30, sticky='w')

    buttonDateOfDeparture = customtkinter.CTkButton(master=frame4, text='SUBMIT DATE', fg_color=c.details, command=lambda: submitDepartureDate(
        dateDeparture, calDateOfDeparture, labelSelectedDate, buttonFuture, buttonYearAgo, buttonFake2, buttonFake1))
    buttonDateOfDeparture.grid(
        column=2, row=2, columnspan=3, padx=30, sticky='w')

    labelSelectedDate.grid(column=2, row=3, columnspan=3, padx=30, sticky='w')

    frameForecast.grid(row=4, column=0, columnspan=5, pady=15)


windll.shcore.SetProcessDpiAwareness(1)



        

# INITIALIZATION
# window
window = tk.Tk()

window.title('WanderWisely')


window.geometry("918x700")

window.minsize(918, 700)

# set maximum window size value
window.maxsize(918, 700)
window.configure(background=c.bgColor)

c.titleFont = tkinter.font.Font(family="Lato", size=13, weight="bold")
c.questionFont = tkinter.font.Font(family="Lato", size=11, weight="bold")
c.errorFont = tkinter.font.Font(family="Lato", size=9, weight="bold")

appearance()

frame1 = InitializationFrame(window)
frame2 = InitializationFrame(window)
frame3 = InitializationFrame(window)
frame4 = InitializationFrame(window)

c.countryName = tk.StringVar(value='your country')
c.baseCurrency = tk.StringVar(value='your base currency')
c.dateStart = tk.StringVar()
c.dateEnd = tk.StringVar()

for frame in (frame1, frame2, frame3, frame4):

    frame.grid(row=0, column=0, sticky='nsew')


for frame in (frame2, frame3, frame4):
    clearView(frame)
gen = counterFrame1()
loadFrame1()

window.mainloop()'''




class FrameBase(tk.Frame):

    def __init__(self, masterWindow, colorOfBg, **kwargs):
        super().__init__(master=masterWindow, bg=colorOfBg,
                         highlightbackground=colorOfBg, highlightcolor=colorOfBg, **kwargs)


class Frame1(FrameBase):

    def __init__(self, masterWindow, colorOfBg):
        super().__init__(masterWindow=masterWindow, colorOfBg=colorOfBg)
        self.gen = counterFrame1()
        self.errorLabel = None
        

        self.load()

    def setFrames(self, frame1, frame2, frame3, frame4):
        self.frame1 = frame1
        self.frame2 = frame2
        self.frame3 = frame3
        self.frame4 = frame4

    def load(self):
        def searchButton():
            countryToFind = c.countryName.get().capitalize()
            global codeCurrency, baseCurrName
            baseCurrName = c.baseCurrency.get().upper()
            codeCurrency = checkingCurrency(countryToFind).upper()
            baseCurrName = checkingBase(baseCurrName)

            if codeCurrency == 'COUNTRYERROR':
                countryError = 'You have entered wrong name of country. Please try again (check full name of country)'
                self.errorLabel = tk.Label(
                    master=self.frameQuestions, text=countryError, font=c.errorFont, bg=c.bgColor, fg='white')
                self.errorLabel.grid(column=0, row=1, columnspan=2)
                self.frameQuestions.after(5000, self.errorLabel.destroy)
            else:
                self.frameCurrency.title['text'] = f'Analyse changes in {codeCurrency}'
                self.fake1.destroy()
                self.fake2.destroy()
                self.fake3.destroy()
                self.buttonLoadFrame2.pack(side=tk.BOTTOM)

                self.buttonLoadFrame3.pack(side=tk.BOTTOM)

                self.buttonLoadFrame4.pack(side=tk.BOTTOM)

                if 'baseCurrName' in globals():
                    params = {'base': baseCurrName, 'symbols': codeCurrency}
                    r = requests.get(
                        'https://api.exchangerate.host/latest/', params)
                    try:
                        data = r.json()
                    except json.JSONDecodeError:
                        print('Wrong format of data.')
                    else:
                        c.current = data["rates"][codeCurrency]
                        self.labelCurrentRate['text'] = f'Current rate: {c.current} {baseCurrName}'

        self.tkraise()

        nr = next(self.gen)

        # title
        self.labelTitle = tk.Label(master=self, text="Let's prepare for your trip!",
                              font=c.titleFont, bg=c.bgColor, fg='white')

        # fields to enter destination and base currency
        self.frameQuestions = tk.Frame(master=self, width=100,  bg=c.bgColor,
                                  highlightbackground=c.bgColor, highlightcolor=c.bgColor)

        self.labelCountry = tk.Label(master=self.frameQuestions, text="What country is your destination?",
                                width=30, font=c.questionFont, bg=c.bgColor, fg='white', anchor="w")
        self.labelCountry.grid(column=0, row=0, pady=10)

        self.entryCountry = tk.Entry(master=self.frameQuestions,
                                width=20, textvariable=c.countryName)
        self.entryCountry.grid(column=1, row=0, pady=10, padx=5)

        self.labelBaseCurrency = tk.Label(master=self.frameQuestions, text="What is your base currency?",
                                     width=30, font=c.questionFont, bg=c.bgColor, fg='white', anchor="w")
        self.labelBaseCurrency.grid(column=0, row=2, pady=10)

        self.entryCurrency = tk.Entry(master=self.frameQuestions,
                                 width=20, textvariable=c.baseCurrency)
        self.entryCurrency.grid(column=1, row=2, pady=10, padx=5)

        self.frameSections = tk.Frame(master=self, width=300, bg=c.bgColor,
                                 highlightbackground=c.bgColor, highlightcolor=c.bgColor)

        self.frameCurrency = ThemeSection(self.frameSections, 100, 300)
        self.frameCurrency.addTitleLabel(title='Changes in currency')
        self.frameCurrency.grid(column=0, row=0, sticky='nsew')
        self.frameCurrency.addImage('cash.png')

        self.labelCurrentRate = tk.Label(
            master=self.frameCurrency, text='Current rate:', bg=c.highlight, font=c.errorFont, fg='white')

        # flights
        self.frameFlights = ThemeSection(self.frameSections, 100, 300)

        self.frameFlights.addTitleLabel(title='Geographical details')
        self.frameFlights.grid(column=1, row=0, sticky='nsew')
        self.frameFlights.addImage('plane.png')

        # weather
        self.frameWeather = ThemeSection(self.frameSections, 100, 300)
        self.frameWeather.addTitleLabel(title='Check the weather')
        self.frameWeather.grid(column=2, row=0, sticky='nsew')
        self.frameWeather.addImage('sun.png')

        self.fake1 = customtkinter.CTkButton(master=self.frameCurrency, text='CURRENCY', fg_color=c.details,
                                        width=20, state=tk.DISABLED)
        self.fake2 = customtkinter.CTkButton(master=self.frameFlights, text='GEOGRAPHY', fg_color=c.details,
                                        width=20, state=tk.DISABLED)
        self.fake3 = customtkinter.CTkButton(master=self.frameWeather, text='WEATHER', fg_color=c.details,
                                        width=20, state=tk.DISABLED)

        self.buttonLoadFrame2 = customtkinter.CTkButton(master=self.frameCurrency, text='CURRENCY', fg_color=c.details,
                                                   width=20, command=lambda: loadFrame(self.frame1, self.frame2.load()))
        self.buttonLoadFrame3 = customtkinter.CTkButton(master=self.frameFlights, text='GEOGRAPHY', fg_color=c.details,
                                                   width=20, command=lambda: loadFrame(self.frame1, self.frame3.load()))
        self.buttonCountrySearch = customtkinter.CTkButton(
            master=self.frameQuestions, width=8, fg_color=c.highlight, text="SEARCH", command=searchButton)
        self.buttonLoadFrame4 = customtkinter.CTkButton(master=self.frameWeather, text='WEATHER', fg_color=c.details,
                                                   width=20, command=lambda: loadFrame(self.frame1, self.frame4.load()))
        self.buttonCountrySearch.grid(column=0, row=3, columnspan=2, pady=10)

        for widget in (self.labelTitle, self.frameQuestions, self.labelCurrentRate, self.frameSections):
            widget.pack()

        if nr == 1:
            self.fake1.pack(side=tk.BOTTOM)
            self.fake2.pack(side=tk.BOTTOM)
            self.fake3.pack(side=tk.BOTTOM)
        else:
            self.buttonLoadFrame2.pack(side=tk.BOTTOM)
            self.buttonLoadFrame3.pack(side=tk.BOTTOM)
            self.buttonLoadFrame4.pack(side=tk.BOTTOM)


class Frame2(FrameBase):

    def __init__(self, masterWindow, colorOfBg,frame1):
        super().__init__(masterWindow=masterWindow, colorOfBg=colorOfBg)
        
        self.frame1 = frame1
        self.load()

    def load(self):
        self.tkraise()

        self.backButton = customtkinter.CTkButton(master=self, text='BACK', fg_color=c.details, width=40, height=40,
                                             command=lambda: multipleFuncButton(clearEntry(entryStart, entryEnd), loadFrame(self, self.frame1.load())))
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
                                                    command=lambda: confirmButton(self, c.dateStart, c.dateEnd, baseCurrName, codeCurrency, fake1, fake2, fake3, buttonPlot1, buttonPlot2, buttonPlot3))
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


class Frame3(FrameBase):

    def __init__(self, masterWindow, colorOfBg,frame1):
        super().__init__(masterWindow=masterWindow, colorOfBg=colorOfBg)
        
        self.frame1 = frame1
        self.load()

    def load(self):
        self.tkraise()
        self.frameOptions = tk.Frame(self, bg=c.highlight)
        self.backButton = customtkinter.CTkButton(master=self, text='BACK', fg_color=c.details, width=40, height=40,
                                             command=lambda: loadFrame(self, self.frame1.load()))
        self.backButton.pack(side=TOP, anchor=NW)

        self.labelTitle = tk.Label(master=self, text=f"Discover some geographical facts about {c.countryName.get().capitalize()}",
                              font=c.titleFont, bg=c.bgColor, fg='white')
        self.labelTitle.pack()
        self.frameOptions.pack()

        self.labelDepartureCountry = tk.Label(master=self.frameOptions, text="What is your departure country?",
                                         width=30, font=c.questionFont, bg=c.bgColor, fg='white', anchor="w")
        self.labelDepartureCountry.grid(column=0, row=0)

        self.departureCountry = tk.StringVar(value='country')

        self.entryDepartureCountry = tk.Entry(
            master=self.frameOptions, textvariable=self.departureCountry)
        self.entryDepartureCountry.grid(column=0, row=1)

        self.labelUnit = tk.Label(master=self.frameOptions, text='Select the unit in which the distance will be displayed',
                             font=c.questionFont, bg=c.bgColor, fg='white', anchor="w")
        self.labelUnit.grid(column=1, row=0, columnspan=2)

        var = tk.StringVar(value='kilometers')

        self.kmButton = tk.Radiobutton(
            master=self.frameOptions, text='kilometers', variable=var, value='kilometers', bg='#9dc0d1')
        self.milesButton = tk.Radiobutton(
            master=self.frameOptions, text='miles', variable=var, value='miles', bg='#9dc0d1')

        self.kmButton.grid(column=1, row=1, pady=5)
        self.milesButton.grid(column=2, row=1, pady=5)

        self.frameCities = tk.Frame(self, bg=c.highlight, height=450)
        self.frameCities.pack(side=LEFT, anchor='n', padx=55, pady=10)
        self.preparingLabelCities(self.frameCities)
        self.frameCheckbutton = tk.Frame(
            master=self, bg='#9dc0d1', width=300, height=450)

        img = (PIL.Image.open("globe.png"))

        resized_image = img.resize((300, 300))
        new_image = ImageTk.PhotoImage(resized_image)

        self.pictureWidget = tk.Label(
            master=self.frameCheckbutton, image=new_image, width=300, height=300, bg=c.bgColor)

        self.pictureWidget.image = new_image
        self.pictureWidget.pack()

        self.frameCheckbutton.pack(side=LEFT, pady=30, anchor='n')

        self.buttonConfirmCountry = customtkinter.CTkButton(master=self.frameOptions, text='CONFIRM COUNTRY', fg_color=c.details,
                                                       command=lambda: confirmCountry(self.departureCountry, self.frameCheckbutton, var.get()))
        self.buttonConfirmCountry.grid(row=2, column=0, columnspan=3, pady=20)

    def preparingLabelCities(self, frame):
        self.destinationGeoInfo = self.searchInfoAboutDestination()
        print(self.destinationGeoInfo)

        capital = self.destinationGeoInfo.get('capital', 'No capital found')
        cities = [city for city in self.destinationGeoInfo['citiesPopulation']]
        population = [self.destinationGeoInfo['citiesPopulation'][city]
                    for city in self.destinationGeoInfo['citiesPopulation']]
        print(cities)
        print(capital)
        print(population)

        self.labelCapital = tk.Label(
            frame, text=f'Capital: {capital}', font=c.questionFont, bg=c.details, fg='white')
        if len(cities) >= 5 and len(population) >= 5:
            self.labelCities = tk.Label(
                frame, text=f'''The most crowded cities:
                \n{cities[0]}, population: {population[0]}
                \n{cities[1]}, population: {population[1]}
                \n{cities[2]}, population: {population[2]}
                \n{cities[3]}, population: {population[3]}
                \n{cities[4]}, population: {population[4]}''', font=c.questionFont, bg=c.highlight, fg='white', justify='left')
        else:
            # Obsłuż sytuację, gdy lista nie ma wystarczającej liczby elementów
            self.labelCities = tk.Label(
                frame, text="Not enough data available for cities.", font=c.questionFont, bg=c.highlight, fg='white')
        self.labelCapital.pack(pady=10, padx=30)
        self.labelCities.pack(pady=10, padx=30)

    def searchInfoAboutDestination(self):
        country = c.countryName.get().capitalize()
        self.fiveCitiesExamples = dict()
        cnt = 0
        self.dictInfo = dict()
        print(country)
        with open('worldcities.csv', encoding='utf8') as csvFile:
            csvRead = csv.reader(csvFile, delimiter=',')
            for row in csvRead:
                if row[4] == country:
                    self.dictInfo['iso'] = row[5]
                    if cnt < 5:
                        self.fiveCitiesExamples[row[1]] = row[9]
                        cnt += 1
                    if row[8] == 'primary':
                        self.dictInfo['capital'] = row[1]
                        self.dictInfo['lat'] = row[2]
                        self.dictInfo['lng'] = row[3]
            self.dictInfo['citiesPopulation'] = self.fiveCitiesExamples
        return self.dictInfo



class Frame4(FrameBase):

    def __init__(self, masterWindow, colorOfBg,frame1):
        super().__init__(masterWindow=masterWindow, colorOfBg=colorOfBg)
        
        self.frame1 = frame1
        self.load()

    def load(self):
        self.tkraise()

        self.backButton = customtkinter.CTkButton(master=self, text='BACK', fg_color=c.details, width=40, height=40,
                                             command=lambda: loadFrame(self, self.frame1.load()))
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
            master=self.frameForecast, text='YEAR AGO', fg_color=c.details, command=lambda: createPlotWeatherYearAgo(self.frameForecast, pastData, self.pictureWidget))
        self.buttonFuture = customtkinter.CTkButton(
            master=self.frameForecast, text='NEXT WEEK', fg_color=c.details,  command=lambda: createPlotWeatherCurrent(self.frameForecast, futureData, self.pictureWidget))

        self.labelTitle = tk.Label(master=self, text="Check the weather",
                              font=c.titleFont, bg=c.highlight, fg='white')
        self.labelTitle.grid(column=2, row=1, columnspan=3, padx=30, sticky='w')

        self.buttonDateOfDeparture = customtkinter.CTkButton(master=self, text='SUBMIT DATE', fg_color=c.details, command=lambda: submitDepartureDate(
            self.dateDeparture, self.calDateOfDeparture, self.labelSelectedDate, self.buttonFuture, self.buttonYearAgo, self.buttonFake2, self.buttonFake1))
        self.buttonDateOfDeparture.grid(
            column=2, row=2, columnspan=3, padx=30, sticky='w')

        self.labelSelectedDate.grid(
            column=2, row=3, columnspan=3, padx=30, sticky='w')

        self.frameForecast.grid(row=4, column=0, columnspan=5, pady=15)


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
        c.countryName = tk.StringVar(value='your country')
        c.baseCurrency = tk.StringVar(value='your base currency')
        c.dateStart = tk.StringVar()
        c.dateEnd = tk.StringVar()

        c.titleFont = tkinter.font.Font(family="Lato", size=13, weight="bold")
        c.questionFont = tkinter.font.Font(family="Lato", size=11, weight="bold")
        c.errorFont = tkinter.font.Font(family="Lato", size=9, weight="bold")
        self.start()
        appearance()

    def start(self):
        self.frame1 = Frame1(self, self.bgColor)
        self.frame2 = Frame2(self, self.bgColor, self.frame1)
        self.frame3 = Frame3(self, self.bgColor, self.frame1)
        self.frame4 = Frame4(self, self.bgColor, self.frame1)

        self.frame1.setFrames(self.frame1, self.frame2,
                              self.frame3, self.frame4)

        for frame in (self.frame1, self.frame2, self.frame3, self.frame4):

            frame.grid(row=0, column=0, sticky='nsew')
        
        
        self.frame1.grid(row=0, column=0, sticky='nsew')
        self.frame2.grid_remove()  # Ukryj ramkę 2
        self.frame3.grid_remove()  # Ukryj ramkę 3
        self.frame4.grid_remove()
        '''for frame in (self.frame2, self.frame3, self.frame4):
            clearView(frame)'''

    
    def clearView(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()


windll.shcore.SetProcessDpiAwareness(1)


app = Window()

app.mainloop()
