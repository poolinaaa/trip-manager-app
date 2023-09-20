import datetime
import config as c
import requests
import json
import tkinter as tk
from tkinter import *
from sqlite3 import *
import csv
from geoFunc import createTable

from datetime import datetime


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


def savingLandmarks(listAttractions):
    createTable('attractionsDatabase', 'attractionsTable')
    for enum, landmark in enumerate(listAttractions):

        landmark.insertIntoDatabase('attractionsTable', 'attractionsDatabase')
        print(enum)
        print('saved')
        if landmark.var.get() == 1:
            landmark.openInTheBrowser()


def submitDepartureDate(dateDeparture, cal, labelSelectedDate, buttonFuture, buttonYearAgo, btn1, btn2):
    btn1.destroy()
    btn2.destroy()
    c.dateFlight = cal.get_date()
    print(c.dateFlight)
    labelSelectedDate['text'] = f'Selected date of departure: {c.dateFlight}'
    buttonFuture.grid(column=0, row=0, sticky='e')
    buttonYearAgo.grid(column=1, row=0, sticky='w')


def appearance():
    c.bgColor = '#295873'
    c.highlight = '#1c3c4f'
    c.details = '#162f3d'


def preparingData(data: dict, codeCurrency):
    c.dates = [date for date in data['rates']]
    c.rate = [data['rates'][date][codeCurrency] for date in data['rates']]
    c.eur = [data['rates'][date]['EUR'] for date in data['rates']]
    c.usd = [data['rates'][date]['USD'] for date in data['rates']]
    c.pln = [data['rates'][date]['PLN'] for date in data['rates']]
    c.cny = [data['rates'][date]['CNY'] for date in data['rates']]


def checkDate(date):
    try:
        isDateCorrect = datetime.strptime(date, '%Y-%m-%d')
        return True
    except:
        return False


def confirmButton(frame, dateStart, dateEnd, baseCurrName, codeCurrency, fake1, fake2, fake3, btn1, btn2, btn3):

    start = dateStart.get()
    end = dateEnd.get()
    if (checkDate(start) and checkDate(end)):
        params = {'start_date': start, 'end_date': end,
                  'base': baseCurrName, 'symbols': f'{codeCurrency},EUR,USD,PLN,CNY'}
        r = requests.get('https://api.exchangerate.host/timeseries/', params)
        print(r)
        try:
            currencyData = r.json()
        except json.JSONDecodeError:
            print('Wrong format of c.currencyData.')
        else:
            print(currencyData)
            preparingData(currencyData, codeCurrency)
            fake1.destroy()
            fake2.destroy()
            fake3.destroy()
            btn1.grid(column=0, row=1, padx=15, pady=10)
            btn2.grid(column=0, row=1, padx=15, pady=10)
            btn3.grid(column=0, row=1, padx=15, pady=10)

    else:
        incorrectDate = tk.Label(
            master=frame, text='wrong format of date, try again', font=c.errorFont, bg=c.highlight, fg='white')
        incorrectDate.pack()
        frame.after(5000, incorrectDate.destroy)
