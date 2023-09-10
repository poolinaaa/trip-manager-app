import tkinter.font
import requests
import json
import tkinter as tk
from currencyFunc import checkingCurrency, checkingBase
from ctypes import windll
from partialForms import ThemeSection, InitializationFrame
from funcBehaviorFrames import counterFrame1, appearance, preparingLabelCities, confirmCountry, clearView, loadFrame, confirmButton, submitDepartureDate, clearEntry, multipleFuncButton
import config as c
from funcPlots import createPlotButton, createPlotButtonAll, createPlotButtonLastMonth
from plotsWeather import createPlotWeatherCurrent, createPlotWeatherYearAgo
from tkcalendar import *
import customtkinter
from tkinter import *


# main frame: menu
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

    
    
    
    for widget in (labelTitle, frameQuestions, labelCurrentRate,frameSections):
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
                                                command=lambda: confirmButton(frame2, c.dateStart, c.dateEnd, baseCurrName, codeCurrency))
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

    labelPlot1 = tk.Label(
        master=framePlots, text='Comparison to the current rate', bg=c.bgColor, fg='white')
    labelPlot1.grid(column=0, row=0, padx=15)

    buttonPlot1 = customtkinter.CTkButton(master=framePlots, width=20, text='SHOW PLOT 1', fg_color=c.details,
                                          command=lambda: createPlotButton(c.dates, c.rate, c.current, framePlots))
    buttonPlot1.grid(column=0, row=1, padx=15, pady=10)

    labelPlot2 = tk.Label(
        master=framePlots, text='Rate compared to changes \nin EUR, USD, PLN, GBP', bg=c.bgColor, fg='white')
    labelPlot2.grid(column=1, row=0, padx=15)

    buttonPlot2 = customtkinter.CTkButton(master=framePlots, width=20, text='SHOW PLOT 2', fg_color=c.details, command=lambda: createPlotButtonAll(
        c.dates, framePlots, c.rate, c.eur, c.usd, c.pln, c.gbp))
    buttonPlot2.grid(column=1, row=1, padx=15, pady=10)

    labelPlot3 = tk.Label(
        master=framePlots, text='Currency rate for the last 30 days', bg=c.bgColor,  fg='white')
    labelPlot3.grid(column=2, row=0, padx=15)

    buttonPlot3 = customtkinter.CTkButton(master=framePlots, width=20, text='SHOW PLOT 3', fg_color=c.details,
                                          command=lambda: createPlotButtonLastMonth(baseCurrName, codeCurrency, framePlots))
    buttonPlot3.grid(column=2, row=1, padx=15, pady=10)

    framePlots.pack()


# frame with flights


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
        master=frameOptions, text='kilometers', variable=var, value='kilometers', bg=c.highlight, fg='white')
    milesButton = tk.Radiobutton(
        master=frameOptions, text='miles', variable=var, value='miles', bg=c.highlight, fg='white')

    kmButton.grid(column=1, row=1)
    milesButton.grid(column=2, row=1)

    frameCities = tk.Frame(frame3, bg=c.highlight)
    frameCities.pack(side=LEFT, padx=50, pady=30)
    preparingLabelCities(frameCities)
    frameCheckbutton = tk.Frame(master=frame3, bg=c.highlight, width=300)

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
        master=frame4, text=f'Selected date of departure: ', font=c.titleFont, bg=c.highlight, fg='white')

    frameForecast = tk.Frame(master=frame4, bg=c.bgColor,
                             highlightbackground=c.bgColor, highlightcolor=c.bgColor)
    buttonYearAgo = customtkinter.CTkButton(
        master=frameForecast, text='YEAR AGO', fg_color=c.details, command=lambda: createPlotWeatherYearAgo(frameForecast, pastData))
    buttonFuture = customtkinter.CTkButton(
        master=frameForecast, text='NEXT MONTH', fg_color=c.details,  command=lambda: createPlotWeatherCurrent(frameForecast, futureData))

    labelTitle = tk.Label(master=frame4, text="Check the weather",
                          font=c.titleFont, bg=c.highlight, fg='white')
    labelTitle.grid(column=2, row=1, columnspan=3, padx=30, sticky='w')

    buttonDateOfDeparture = customtkinter.CTkButton(master=frame4, text='SUBMIT DATE', fg_color=c.details, command=lambda: submitDepartureDate(
        dateDeparture, calDateOfDeparture, labelSelectedDate, buttonFuture, buttonYearAgo))
    buttonDateOfDeparture.grid(
        column=2, row=2, columnspan=3, padx=30, sticky='w')

    labelSelectedDate.grid(column=2, row=3, columnspan=3, padx=30, sticky='w')
    frameForecast.grid(row=4, column=0, columnspan=5, pady=15)


windll.shcore.SetProcessDpiAwareness(1)


# INITIALIZATION
# window
window = tk.Tk()

window.title('Travel advisor')

x = 550
y = 200
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

window.mainloop()
