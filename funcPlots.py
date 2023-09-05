
import requests
import json
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import date, timedelta


def preparingPastData(pastData: dict):
    days = pastData['daily']['time']
    temperature = pastData['daily']['temperature_2m_mean']
    return days, temperature


def createPlotWeatherYearAgo(parent, pastData):
    x, y = preparingPastData(pastData)
    fig = Figure(figsize=(3, 3), dpi=100)
    plotPast = fig.add_subplot(111)

    plotPast.plot(list(range(0, len(x))), y,)
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack()

def preparingCurrentData(futureData: dict):
    time = futureData['hourly']['time']
    temperature = futureData['hourly']['temperature_2m']
    precipitationProb=futureData['hourly']['precipitation_probability']
    precipitation=futureData['hourly']['precipitation']
    
    return time, temperature, precipitationProb, precipitation


def createPlotWeatherCurrent(parent, futureData):
    x, y, y1, y2 = preparingCurrentData(futureData)
    xRange = list(range(0, len(x)))
    fig = Figure(figsize=(3, 3), dpi=100)
    
    plotCurrentTemp = fig.add_subplot(111)
    plotCurrentTemp.plot(xRange, y, xRange, y1, xRange, y2)

    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack()

def createPlotButton(dates, rates, current, parent):
    y = rates
    x = {num: date for num, date in enumerate(dates)}
    currRate = [current for _ in range(len(dates))]

    fig = Figure(figsize=(3, 3), dpi=100)
    plot1 = fig.add_subplot(111)

    plot1.plot(list(range(0, len(dates))), y,
               list(range(0, len(dates))), currRate)
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=1, columnspan=3)


def createPlotButtonAll(dates, parent, ratesChosenCountry, EUR, USD, PLN, GBP):
    y = ratesChosenCountry
    x = {num: date for num, date in enumerate(dates)}
    ox = list(range(0, len(dates)))
    e = EUR
    u = USD
    p = PLN
    g = GBP
    # the figure that will contain the plot
    fig = Figure(figsize=(3, 3), dpi=100)

    plot1 = fig.add_subplot(111)

    plot1.plot(ox, y, ox, e, ox, u, ox, p, ox, g)
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=1, columnspan=3)


def createPlotButtonLastMonth(baseCurrName, codeCurrency, parent):

    today = date.today()
    monthAgo = today - timedelta(days=30)

    params = {'start_date': monthAgo, 'end_date': today,
              'base': baseCurrName, 'symbols': codeCurrency}
    r = requests.get('https://api.exchangerate.host/timeseries/', params)
    print(r)
    try:
        currencyData = r.json()
    except json.JSONDecodeError:
        print('Wrong format of data.')
    else:
        print(currencyData)
        dates = [date for date in currencyData['rates']]
        rate = [currencyData['rates'][date][codeCurrency]
                for date in currencyData['rates']]
        y = rate
        x = {num: date for num, date in enumerate(dates)}

        fig = Figure(figsize=(3, 3), dpi=100)
        plot1 = fig.add_subplot(111)

        plot1.plot(list(range(0, len(dates))), y)
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=1, columnspan=3)
