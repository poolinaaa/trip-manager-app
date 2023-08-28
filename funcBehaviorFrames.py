
import config as c
import requests
import json
import tkinter as tk
from tkinter import *
import csv
from geoFunc import getDistanceBetweenPoints, searchAttractions
from classes import Landmark


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


def confirmCountry(strVarCountry, frame):
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
            latBase, lngBase, destinationGeoInfo['lat'], destinationGeoInfo['lng'])
        print(distance)

        attractions = searchAttractions(
            destinationGeoInfo['lng'], destinationGeoInfo['lat'])
        
        listOfAttractions = list()

        for attraction in attractions['features']:
            landmark = Landmark(attraction['properties']['address_line1'],
                                attraction['properties']['address_line2'],
                                attraction['properties']['datasource']['raw']['image'])
            listOfAttractions.append(landmark)
            landmark.checkboxButton(frame)
        
        frame.pack()





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



