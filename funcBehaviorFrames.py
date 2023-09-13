import datetime
import config as c
import requests
import json
import tkinter as tk
from tkinter import *
from sqlite3 import *
import csv
from geoFunc import getDistanceBetweenPoints, searchAttractions, createTable
import webbrowser
import customtkinter

from datetime import datetime


class AttractionToSee:
    AttractionToSeeId = 1

    def __init__(self, name, address, link=None):
        self.name = name
        self.address = address
        self.link = link

        self.id = AttractionToSee.AttractionToSeeId
        AttractionToSee.AttractionToSeeId += 1

    def checkboxButton(self, frame):
        self.var = tk.IntVar()
        self.button = tk.Checkbutton(
            master=frame, text=f'{self.name}', variable=self.var, onvalue=1, offvalue=0, justify='left',bg='#9dc0d1',font=c.errorFont)
        self.button.pack(anchor='w')

    def insertIntoDatabase(self, table, database):
        try:
            con = connect(f'{database}.db')
            cur = con.cursor()
            print("connected")

            insertAttraction = f"""INSERT INTO {table}
                            (nameOfAttraction,address, wantToSee) 
                            VALUES (?, ?, ?);"""
            if self.var.get() == 1:
                data = (self.name, self.address, 'yes')
            else:
                data = (self.name, self.address, 'no')

            cur.execute(insertAttraction, data)
            con.commit()
            print("success")

            cur.close()

        except Error as error:
            print("fail", error)

        finally:
            if con:
                con.close()
                print("connection is closed")

    def openInTheBrowser(self):
        if self.name != None:
            url = "https://www.google.com.tr/search?q={}".format(self.name)
            webbrowser.open_new_tab(url)
        else:
            print('There is not any link')


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


def searchInfoAboutDestination():
    country = c.countryName.get().capitalize()
    fiveCitiesExamples = dict()
    cnt = 0
    dictInfo = dict()
    print(country)
    with open('worldcities.csv', encoding='utf8') as csvFile:
        csvRead = csv.reader(csvFile, delimiter=',')
        for row in csvRead:
            if row[4] == country:
                dictInfo['iso'] = row[5]
                if cnt < 5:
                    fiveCitiesExamples[row[1]] = row[9]
                    cnt += 1
                if row[8] == 'primary':
                    dictInfo['capital'] = row[1]
                    dictInfo['lat'] = row[2]
                    dictInfo['lng'] = row[3]
        dictInfo['citiesPopulation'] = fiveCitiesExamples
    return dictInfo


def savingLandmarks(listAttractions):
    createTable('attractionsDatabase', 'attractionsTable')
    for enum, landmark in enumerate(listAttractions):

        landmark.insertIntoDatabase('attractionsTable', 'attractionsDatabase')
        print(enum)
        print('saved')
        if landmark.var.get() == 1:
            landmark.openInTheBrowser()


def confirmCountry(strVarCountry, frame, unit, frameToDestroy):
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

        destinationGeoInfo = searchInfoAboutDestination()
        print(destinationGeoInfo)

        distance = getDistanceBetweenPoints(
            latBase, lngBase, destinationGeoInfo['lat'], destinationGeoInfo['lng'], unit)

        distanceLabel = tk.Label(
            master=frame, text=f'Distance between {baseCountry} and {c.countryName.get().capitalize()} is about \n{distance} {unit}', font=c.questionFont, bg=c.highlight, fg='white', anchor="w")
        distanceLabel.pack()

        attractions = searchAttractions(
            destinationGeoInfo['lng'], destinationGeoInfo['lat'])

        listOfAttractions = list()

        for attr in attractions['features']:
            ds = attr['properties']['datasource']
            raw = ds.get('raw', {})  # Handle if 'raw' key is missing
            image_url = raw.get('image', '')
            landmark = AttractionToSee(attr['properties']['address_line1'],
                                       attr['properties']['address_line2'],
                                       image_url)
            listOfAttractions.append(landmark)
            landmark.checkboxButton(frame)

        buttonSave = customtkinter.CTkButton(master=frame, text='SAVE IN THE DATABASE', fg_color=c.details,
                                             command=lambda: savingLandmarks(listOfAttractions))
        buttonSave.pack(pady=10)
        frameToDestroy.destroy()
        frame.pack(side=LEFT, pady=10, anchor='nw')


def submitDepartureDate(dateDeparture, cal, labelSelectedDate, buttonFuture, buttonYearAgo):
    
    c.dateFlight = cal.get_date()
    print(c.dateFlight)
    labelSelectedDate['text'] = f'Selected date of departure: {c.dateFlight}'
    buttonFuture.grid(column=0, row=0, sticky='e')
    buttonYearAgo.grid(column=1, row=0, sticky = 'w')


def multipleFuncButton(*functions):
    def executingFunctions(*args, **kwargs):
        for func in functions:
            func(*args, **kwargs)
        return executingFunctions


def clearEntry(*entries):
    for entry in entries:
        entry.delete(0, tk.END)


def clearView(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def loadFrame(frameToClear, funcRaisingFrame):
    clearView(frameToClear)
    funcRaisingFrame()


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
    c.gbp = [data['rates'][date]['GBP'] for date in data['rates']]


def checkDate(date):
    try:
        isDateCorrect = datetime.strptime(date, '%Y-%m-%d')
        return True
    except:
        return False


def confirmButton(frame, dateStart, dateEnd, baseCurrName, codeCurrency):

    start = dateStart.get()
    end = dateEnd.get()
    if (checkDate(start) and checkDate(end)):
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

    else:
        incorrectDate = tk.Label(
            master=frame, text='wrong format of date, try again', font=c.errorFont, bg=c.highlight, fg='white')
        incorrectDate.pack()
        frame.after(5000, incorrectDate.destroy)


def preparingLabelCities(frame):
    destinationGeoInfo = searchInfoAboutDestination()
    print(destinationGeoInfo)

    capital = destinationGeoInfo['capital']
    cities = [city for city in destinationGeoInfo['citiesPopulation']]
    population = [destinationGeoInfo['citiesPopulation'][city]
                  for city in destinationGeoInfo['citiesPopulation']]
    print(cities)
    print(capital)
    print(population)

    labelCapital = tk.Label(
        frame, text=f'Capital: {capital}', font=c.questionFont, bg=c.details, fg='white')
    labelCities = tk.Label(
        frame, text=f'''The most crowded cities:
        \n{cities[0]}, population: {population[0]}
        \n{cities[1]}, population: {population[1]}
        \n{cities[2]}, population: {population[2]}
        \n{cities[3]}, population: {population[3]}
        \n{cities[4]}, population: {population[4]}''', font=c.questionFont, bg=c.highlight, fg='white', justify='left')
    labelCapital.pack(pady=10, padx=30)
    labelCities.pack(pady=10, padx=30)


def counterFrame1():
    i = 1
    while True:
        yield i
        i += 1
