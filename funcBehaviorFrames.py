from ast import Dict, List
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

def checkingCountry(country):
    with open('countries.csv', encoding='utf8') as csvFile:
        csvRead = csv.reader(csvFile, delimiter=',')
        for row in csvRead:
            if row[2] == country:
                foundCountry = row[2]
                
        if 'foundCountry' not in locals():
            return 'CountryError'
        else:
            return foundCountry


                           

def searchInfo():
    country = c.countryName.get().capitalize()
    fiveCitiesExamples = Dict()
    cnt = 0
    dictInfo = dict()
    print(country)
    with open('worldcities.csv', encoding='utf8') as csvFile:
        csvRead = csv.reader(csvFile, delimiter=',')
        for row in csvRead:
            if row[4] == country:
                dictInfo['iso'] = row[5]
                if cnt < 5:
                    fiveCitiesExamples[row[1]]=row[9]
                    cnt += 1
                if row[8]=='primary':
                    dictInfo['capital']=row[1]
                    dictInfo['lat']=row[2]
                    dictInfo['lng']=row[3]
        dictInfo['citiesPopulation']=fiveCitiesExamples
    return dictInfo
                    
def confirmCountry(strVarCountry):
    baseCountry = strVarCountry.get().capitalize()
    baseCountry = checkingCountry(baseCountry)

    with open('worldcities.csv', encoding='utf8') as csvFile:
        csvRead = csv.reader(csvFile, delimiter=',')
        for row in csvRead:
            if row[4] == baseCountry:
                isoBase = row[5]
                latBase = row[2]
                lngBase = row[3]
                break
        destinationGeoInfo = searchInfo()              
                



def submitDepartureDate(dateFlight, cal, labelSelectedDate):
    dateFlight = cal.get_date()
    print(dateFlight)
    labelSelectedDate['text'] = f'Selected date of departure: {str(dateFlight)[0:4]}-{str(dateFlight)[4:6]}-{str(dateFlight)[6:]}'
    

    


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
