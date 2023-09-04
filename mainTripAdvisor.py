import tkinter.font
import requests
import json
import tkinter as tk
from currencyFunc import checkingCurrency, checkingBase
from ctypes import windll
from partialForms import ThemeSection, InitializationFrame
from funcBehaviorFrames import appearance, confirmCountry, clearView, loadFrame, confirmButton, submitDepartureDate
import config as c
from funcPlots import createPlotButton, createPlotButtonAll, createPlotButtonLastMonth
from tkcalendar import *
import customtkinter


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

    buttonCountrySearch = customtkinter.CTkButton(
        master=frameQuestions, width=8, fg_color=c.highlight,text="SEARCH", command=searchButton)
    buttonCountrySearch.grid(column=0, row=3, columnspan=2, pady=10)

    # declare 3 sections of preparing the trip: currency, flights, weather
    frameSections = tk.Frame(master=frame1, width=300, bg=c.bgColor,
                             highlightbackground=c.bgColor, highlightcolor=c.bgColor)

    # currency
    frameCurrency = ThemeSection(frameSections,100,300)
    frameCurrency.addTitleLabel(title='Changes in currency')
    frameCurrency.grid(column=0, row=0, sticky='nsew')
    frameCurrency.addImage('cash.png')

    labelCurrentRate = tk.Label(
        master=frameCurrency, text='Current rate:', bg=c.highlight, font=c.errorFont, fg='white')

    # flights
    frameFlights = ThemeSection(frameSections,100,300)
    
    frameFlights.addTitleLabel(title='Geographical details')
    frameFlights.grid(column=1, row=0, sticky='nsew')
    frameFlights.addImage('plane.png')

    # weather
    frameWeather = ThemeSection(frameSections,100,300)
    frameWeather.addTitleLabel(title='Check the weather')
    frameWeather.grid(column=2, row=0, sticky='nsew')
    frameWeather.addImage('sun.png')

    
    # packing widgets
    for widget in (labelTitle, frameQuestions, labelCurrentRate):
        widget.pack()
    
    frameSections.pack()
    

    # loading buttons
    buttonLoadFrame2 = customtkinter.CTkButton(master=frameCurrency, text='CURRENCY',fg_color=c.details,
                                 width=20, command=lambda: loadFrame(frame1, loadFrame2))
    buttonLoadFrame2.pack(side=tk.BOTTOM)

    buttonLoadFrame3 = customtkinter.CTkButton(master=frameFlights, text='GEOGRAPHY',fg_color=c.details,
                                 width=20, command=lambda: loadFrame(frame1, loadFrame3))
    buttonLoadFrame3.pack(side=tk.BOTTOM)

    buttonLoadFrame4 = customtkinter.CTkButton(master=frameWeather, text='WEATHER',fg_color=c.details,
                                 width=20, command=lambda: loadFrame(frame1, loadFrame4))
    buttonLoadFrame4.pack(side=tk.BOTTOM)
    

# frame with currency rate


def loadFrame2():
    frame2.tkraise()

    labelTitle = tk.Label(master=frame2, text="Analyse currency rate",
                          font=c.titleFont, bg=c.highlight, fg='white')
    labelTitle.pack()

    frameEnteringDate = tk.Frame(master=frame2)
    frameEnteringDate.pack()

    labelStartDate = tk.Label(master=frameEnteringDate,
                              text='Enter the start date: ')
    labelStartDate.grid(column=0, row=0)

    labelEndDate = tk.Label(master=frameEnteringDate,
                            text='Enter the end date: ')
    labelEndDate.grid(column=1, row=0)

    buttonConfirmDate = customtkinter.CTkButton(master=frameEnteringDate, width=20, text='CONFIRM TIME SPAN',fg_color=c.details,
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

    buttonPlot1 = customtkinter.CTkButton(master=framePlots, width=20, text='PLOT',fg_color=c.details,
                            command=lambda: createPlotButton(c.dates, c.rate, c.current, framePlots))
    buttonPlot1.grid(column=0, row=0)

    buttonPlot2 = customtkinter.CTkButton(master=framePlots, width=20, text='PLOT',fg_color=c.details, command=lambda: createPlotButtonAll(
        c.dates, framePlots, c.rate, c.eur, c.usd, c.pln, c.gbp))
    buttonPlot2.grid(column=1, row=0)

    buttonPlot3 = customtkinter.CTkButton(master=framePlots, width=20, text='PLOT',fg_color=c.details,
                            command=lambda: createPlotButtonLastMonth(baseCurrName, codeCurrency, framePlots))
    buttonPlot3.grid(column=2, row=0)

    framePlots.pack()

    backButton = customtkinter.CTkButton(master=frame2, text='BACK',fg_color=c.details,
                           command=lambda: loadFrame(frame2, loadFrame1))
    backButton.pack(side=tk.BOTTOM)

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

    entryDepartureCountry = tk.Entry(
        master=frame3, textvariable=departureCountry)
    entryDepartureCountry.pack()

    labelUnit = tk.Label(master=frame3, text='Select the unit in which the distance will be displayed', width=30, font=c.questionFont, bg=c.bgColor, fg='white', anchor="w")
    labelUnit.pack()

    var = tk.StringVar(value='kilometers')
    
    kmButton = tk.Radiobutton(master=frame3, text='kilometers', variable=var, value='kilometers')
    milesButton = tk.Radiobutton(master=frame3, text='miles', variable=var, value='miles')

    kmButton.pack()
    milesButton.pack()

    frameCheckbutton = tk.Frame(master=frame3, bg=c.highlight)

    buttonConfirmCountry = customtkinter.CTkButton(master=frame3, text='CONFIRM COUNTRY',fg_color=c.details,
                                     command=lambda: confirmCountry(departureCountry, frameCheckbutton, var.get()))
    buttonConfirmCountry.pack()

    backButton = customtkinter.CTkButton(master=frame3, text='BACK',fg_color=c.details,
                           command=lambda: loadFrame(frame3, loadFrame1))
    backButton.pack(side=tk.BOTTOM)

# frame with weather


def loadFrame4():
    frame4.tkraise()
    futureData = tk.StringVar()
    pastData = tk.StringVar()
    
    calDateOfDeparture = Calendar(
        master=frame4, selectmode='day', date_pattern='YYYY-MM-DD')
    calDateOfDeparture.pack()
    dateDeparture = tk.StringVar(value='YYYY-MM-DD')
    labelSelectedDate = tk.Label(
        master=frame4, text=f'Selected date of departure: ', bg=c.bgColor, fg='white')
    
    frameForecast = tk.Frame(master=frame4, bg=c.bgColor, highlightbackground=c.bgColor, highlightcolor=c.bgColor)
    buttonYearAgo = customtkinter.CTkButton(master=frameForecast, text='YEAR AGO', state=tk.DISABLED, fg_color=c.details)
    buttonFuture = customtkinter.CTkButton(master=frameForecast, text='NEXT MONTH', state=tk.DISABLED, fg_color=c.details)
    


    buttonDateOfDeparture = customtkinter.CTkButton(master=frame4, text='SUBMIT DATE', fg_color=c.details, command=lambda: submitDepartureDate(
        dateDeparture, calDateOfDeparture, labelSelectedDate, buttonYearAgo, futureData, pastData))
    buttonDateOfDeparture.pack()
    
    frameForecast.pack()
    buttonFuture.pack()
    buttonYearAgo.pack()
    labelSelectedDate.pack()
    

    backButton = customtkinter.CTkButton(master=frame4, text='BACK', fg_color=c.details,
                           command=lambda: loadFrame(frame4, loadFrame1))
    backButton.pack(side=tk.BOTTOM)


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

    frame.grid(row=0, column=0, sticky='nsew')


for frame in (frame2, frame3, frame4):
    clearView(frame)

loadFrame1()

window.mainloop()
