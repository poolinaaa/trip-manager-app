import tkinter.font
import requests
import json
import tkinter as tk
from currencyFunc import checkingCurrency, checkingBase
from ctypes import windll
from classes import ThemeSection, InitializationFrame
from funcBehaviorFrames import appearance, confirmCountry, clearView, loadFrame, confirmButton, createPlotButton, createPlotButtonAll, createPlotButtonLastMonth, submitDepartureDate
import config as c
from PIL import ImageTk


from datetime import datetime
from tkcalendar import *


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

    # title
    labelTitle = tk.Label(master=frame1, text="Let's prepare for your trip!",
                          font=c.titleFont, bg=c.bgColor, fg='white')

    # fields to enter destination and base currency
    frameQuestions = tk.Frame(master=frame1, pady=0, bg=c.bgColor,
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

    buttonCountrySearch = tk.Button(
        master=frameQuestions, width=8, text="SEARCH", command=searchButton)
    buttonCountrySearch.grid(column=0, row=3, columnspan=2, pady=10)

    # declare 3 sections of preparing the trip: currency, flights, weather
    frameSections = tk.Frame(master=frame1, bg=c.bgColor,
                             highlightbackground=c.bgColor, highlightcolor=c.bgColor)

    # currency
    frameCurrency = ThemeSection(frameSections)
    frameCurrency.addTitleLabel(title='Changes in currency')
    frameCurrency.grid(column=0, row=0, sticky="nsew")
    frameCurrency.addImage('cash.png')

    labelCurrentRate = tk.Label(
        master=frameCurrency, text='Current rate:', bg=c.bgColor, fg='white')

    # flights
    frameFlights = ThemeSection(frameSections)
    frameFlights.addTitleLabel(title='Find proper flight')
    frameFlights.grid(column=1, row=0, sticky="nsew")
    frameFlights.addImage('plane.png')

    # weather
    frameWeather = ThemeSection(frameSections)
    frameWeather.addTitleLabel(title='Check the weather')
    frameWeather.grid(column=2, row=0, sticky="nsew")
    frameWeather.addImage('sun.png')

    # packing widgets
    for widget in (labelTitle, frameQuestions, frameSections, labelCurrentRate):
        widget.pack()

    # loading buttons
    frameSelectTopic = tk.Frame(master=frame1, bg=c.bgColor,
                                highlightbackground=c.bgColor, highlightcolor=c.bgColor)

    buttonLoadFrame2 = tk.Button(master=frameSelectTopic, text='Analyze changes of currency in detail',
                                 width=19, command=lambda: loadFrame(frame1, loadFrame2))
    buttonLoadFrame2.grid(column=0, row=0, padx=12, sticky="nsew")

    buttonLoadFrame3 = tk.Button(master=frameSelectTopic, text='Planessss',
                                 width=19, command=lambda: loadFrame(frame1, loadFrame3))
    buttonLoadFrame3.grid(column=1, row=0, padx=16, sticky="nsew")

    buttonLoadFrame4 = tk.Button(master=frameSelectTopic, text='Weather',
                                 width=19, command=lambda: loadFrame(frame1, loadFrame4))
    buttonLoadFrame4.grid(column=2, row=0, padx=12, sticky="nsew")
    frameSelectTopic.pack()

# frame with currency rate


def loadFrame2():
    frame2.tkraise()

    labelTitle = tk.Label(master=frame2, text="Analyse currency rate",
                          font=c.titleFont, bg=c.bgColor, fg='white')
    labelTitle.pack()

    frameEnteringDate = tk.Frame(master=frame2)
    frameEnteringDate.pack()

    labelStartDate = tk.Label(master=frameEnteringDate,
                              text='Enter the start date: ')
    labelStartDate.grid(column=0, row=0)

    labelEndDate = tk.Label(master=frameEnteringDate,
                            text='Enter the end date: ')
    labelEndDate.grid(column=1, row=0)

    buttonConfirmDate = tk.Button(master=frameEnteringDate, width=20, text='CONFIRM TIME SPAN',
                                  command=lambda: confirmButton(c.dateStart, c.dateEnd, baseCurrName, codeCurrency))
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

    buttonPlot1 = tk.Button(master=framePlots, width=20, text='PLOT',
                            command=lambda: createPlotButton(c.dates, c.rate, c.current, framePlots))
    buttonPlot1.grid(column=0, row=0)

    buttonPlot2 = tk.Button(master=framePlots, width=20, text='PLOT', command=lambda: createPlotButtonAll(
        c.dates, framePlots, c.rate, c.eur, c.usd, c.pln, c.gbp))
    buttonPlot2.grid(column=1, row=0)

    buttonPlot3 = tk.Button(master=framePlots, width=20, text='PLOT',
                            command=lambda: createPlotButtonLastMonth(baseCurrName, codeCurrency, framePlots))
    buttonPlot3.grid(column=2, row=0)

    framePlots.pack()

    backButton = tk.Button(master=frame2, text='BACK',
                           command=lambda: loadFrame(frame2, loadFrame1))
    backButton.pack(pady=20)

# frame with flights


def loadFrame3():
    frame3.tkraise()
    
    labelTitle = tk.Label(master=frame3, text="Find a flight",
                        font=c.titleFont, bg=c.bgColor, fg='white')
    labelTitle.pack()

    labelDepartureCountry = tk.Label(master=frame3, text="What is your departure country?",
                                 width=30, font=c.questionFont, bg=c.bgColor, fg='white', anchor="w")
    labelDepartureCountry.pack()
    departureCountry = tk.StringVar(value='country')

    entryDepartureCountry = tk.Entry(master=frame3, textvariable=departureCountry)
    entryDepartureCountry.pack()

    buttonConfirmCountry = tk.Button(master=frame3, text='CONFIRM COUNTRY', command=lambda : confirmCountry(departureCountry))
    buttonConfirmCountry.pack()
    

    
    backButton = tk.Button(master=frame3, text='BACK',
                           command=lambda: loadFrame(frame3, loadFrame1))
    backButton.pack(pady=20)

# frame with weather


def loadFrame4():
    frame4.tkraise()

    calDateOfDeparture = Calendar(
        master=frame4, selectmode='day', date_pattern='YYYYMMDD')
    calDateOfDeparture.pack()
    dateDeparture = tk.StringVar(value='YYYYMMDD')
    labelSelectedDate = tk.Label(master=frame4, text=f'Selected date of departure: ',bg=c.bgColor, fg='white')
    buttonDateOfDeparture = tk.Button(master=frame4, text='SUBMIT DATE', command=lambda: submitDepartureDate(
        dateDeparture, calDateOfDeparture, labelSelectedDate))
    buttonDateOfDeparture.pack()
    

    labelSelectedDate.pack()

    backButton = tk.Button(master=frame4, text='BACK',
                           command=lambda: loadFrame(frame4, loadFrame1))
    backButton.pack(pady=20)


windll.shcore.SetProcessDpiAwareness(1)


# INITIALIZATION
# window
window = tk.Tk()
window.title('Travel advisor')

x = 600
y = 300
window.geometry("+%d+%d" % (x, y))
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


iata = tk.StringVar()

for frame in (frame1, frame2, frame3, frame4):

    frame.grid(row=0, column=0, sticky="nsew")


for frame in (frame2, frame3, frame4):
    clearView(frame)

loadFrame1()

window.mainloop()
