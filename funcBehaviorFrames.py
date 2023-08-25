import config as c
import requests
import json
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import date, timedelta
import csv

def searchAirport(iata):
    country = c.countryName.get().capitalize()
    with open('worldcities.csv') as csvFile:
        csvRead = csv.reader(csvFile, delimiter=',')
        for row in csvRead:
            if row[4] == country:
                iso = row[5]
                break
    with open('airports.csv') as csvFile1:
        csvRead1 = csv.reader(csvFile1, delimiter=',')
        for row in csvRead1:
            if row[8] == iso:
                iata = row[13]
                break


def searchingFlights(date, airport1, airport2):

    url = f"https://timetable-lookup.p.rapidapi.com/TimeTable/{airport1}/{airport2}/{date}/"

    querystring = {"Sort": "Departure", "Results": "20", "7Day": "Y"}

    headers = {
        "X-RapidAPI-Key": "25d7923676msh76e2082c55923c2p1744a9jsn5eb37ae457be",
        "X-RapidAPI-Host": "timetable-lookup.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())


def submitDepartureDate(dateFlight, cal, frame3):
    dateFlight = cal.get_date()
    print(dateFlight)
    labelSelectedDate = tk.Label(
        master=frame3, text=f'Selected date of departure: {str(dateFlight)[0:4]}-{str(dateFlight)[4:6]}-{str(dateFlight)[6:]}')
    labelSelectedDate.pack()


def clearView(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def loadFrame(frameToClear, funcRaisingFrame):
    clearView(frameToClear)
    funcRaisingFrame()


def appearance():
    c.bgColor = '#3d4660'


def preparingData(data: dict, codeCurrency):
    c.dates = [date for date in data['rates']]
    c.rate = [data['rates'][date][codeCurrency] for date in data['rates']]
    c.eur = [data['rates'][date]['EUR'] for date in data['rates']]
    c.usd = [data['rates'][date]['USD'] for date in data['rates']]
    c.pln = [data['rates'][date]['PLN'] for date in data['rates']]
    c.gbp = [data['rates'][date]['GBP'] for date in data['rates']]


def confirmButton(dateStart, dateEnd, baseCurrName, codeCurrency):
    start = dateStart.get()
    end = dateEnd.get()

    params = {'start_date': start, 'end_date': end,
              'base': baseCurrName, 'symbols': f'{codeCurrency},EUR,USD,PLN,GBP'}
    r = requests.get('https://api.exchangerate.host/timeseries/', params)
    print(r)
    try:
        currencyData = r.json()
    except json.JSONDecodeError:
        print('Wrong format of c.currencyData.')
    else:
        print(currencyData)
        preparingData(currencyData, codeCurrency)


def createPlotButton(dates, rates, current, parent):
    y = rates
    x = {num: date for num, date in enumerate(dates)}
    currRate = [current for _ in range(len(dates))]

    fig = Figure(figsize=(4, 4), dpi=100)
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
    fig = Figure(figsize=(4, 4), dpi=100)

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

        fig = Figure(figsize=(4, 4), dpi=100)
        plot1 = fig.add_subplot(111)

        plot1.plot(list(range(0, len(dates))), y)
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=1, columnspan=3)
