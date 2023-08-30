import config as c
import requests
import json
import tkinter as tk
from tkinter import *
from sqlite3 import *
import csv
from geoFunc import getDistanceBetweenPoints, searchAttractions, createTable
import webbrowser


class AttractionToSee:
    AttractionToSeeId = 1

    def __init__(self, name, address,link=None) :
        self.name = name
        self.address = address
        self.link = link
        
        self.id = AttractionToSee.AttractionToSeeId
        AttractionToSee.AttractionToSeeId += 1

    def checkboxButton(self, frame):
        self.var = tk.IntVar()
        self.button = tk.Checkbutton(master=frame, text=f'{self.name}',variable=self.var, onvalue=1, offvalue=0, justify='left')
        self.button.pack()

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
        if self.link != None:
            webbrowser.open_new_tab(self.link)
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
    createTable( 'attractionsDatabase','attractionsTable')    
    for enum, landmark in enumerate(listAttractions):
        
        landmark.insertIntoDatabase('attractionsTable', 'attractionsDatabase')
        print(enum)
        print('saved')
        if landmark.var.get() == 1:
            landmark.openInTheBrowser()


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

        

        for attr in attractions['features']:
            ds = attr['properties']['datasource']
            raw = ds.get('raw', {})  # Handle if 'raw' key is missing
            image_url = raw.get('image', '')
            landmark = AttractionToSee(attr['properties']['address_line1'],
                                attr['properties']['address_line2'],
                                image_url)
            listOfAttractions.append(landmark)
            landmark.checkboxButton(frame)
        
        buttonSave = tk.Button(master=frame, text='CONFIRM CHOICES', command= lambda : savingLandmarks(listOfAttractions))
        buttonSave.pack()

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
