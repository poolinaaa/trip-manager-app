import json
import requests
from numpy import sin, cos, arccos, pi, round
from tkinter import *
from sqlite3 import *
import csv
import sqlite3 as sql


class GeographyData():
    def savingLandmarks(self, listAttractions):
        self.createTable('attractionsDatabase', 'attractionsTable')
        for enum, landmark in enumerate(listAttractions):

            landmark.insertIntoDatabase(
                'attractionsTable', 'attractionsDatabase')
            print(enum)
            print('saved')
            if landmark.var.get() == 1:
                landmark.openInTheBrowser()

    def createTable(self, nameOfDb, nameOfTable):
        con = sql.connect(f'{nameOfDb}.db')
        cur = con.cursor()
        cur.execute(f'''CREATE TABLE if not exists {nameOfTable} (
                    nameOfAttraction TEXT,
                    address TEXT,
                    wantToSee TEXT)''')
        con.commit()
        cur.execute(f'''DELETE FROM {nameOfTable}''')
        con.commit()
        cur.close()

    def searchInfoAboutDestination(self, countryName) -> dict:
        country = countryName.get().capitalize()
        self.fiveCitiesExamples = dict()
        cnt = 0
        self.dictInfo = dict()
        print(country)
        with open('worldcities.csv', encoding='utf8') as csvFile:
            csvRead = csv.reader(csvFile, delimiter=',')
            for row in csvRead:
                if row[4] == country:
                    self.dictInfo['iso'] = row[5]
                    if cnt < 5:
                        self.fiveCitiesExamples[row[1]] = row[9]
                        cnt += 1
                    if row[8] == 'primary':
                        self.dictInfo['capital'] = row[1]
                        self.dictInfo['lat'] = row[2]
                        self.dictInfo['lng'] = row[3]
            self.dictInfo['citiesPopulation'] = self.fiveCitiesExamples
        return self.dictInfo

    def getDistanceBetweenPoints(self, latitude1, longitude1, latitude2, longitude2, unit='kilometers'):

        theta = float(longitude1) - float(longitude2)

        distance = 60 * 1.1515 * self.rad2deg(
            arccos(
                (sin(self.deg2rad(latitude1)) * sin(self.deg2rad(latitude2))) +
                (cos(self.deg2rad(latitude1)) *
                 cos(self.deg2rad(latitude2)) * cos(self.deg2rad(theta)))
            )
        )

        if unit == 'miles':
            return round(distance, 2)
        if unit == 'kilometers':
            return round(distance * 1.609344, 2)

    def rad2deg(self, radians):
        degrees = float(radians) * 180 / pi
        return degrees

    def deg2rad(self, degrees):
        radians = float(degrees) * pi / 180
        return radians

    def searchAttractions(self, lng, lat):
        url = 'https://api.geoapify.com/v2/places'

        params = dict(categories='tourism.attraction',
                      filter=f'circle:{lng},{lat},5000', limit=10, apiKey='f17cce1b808a4e39845aca4cf631bf04')

        resp = requests.get(url=url, params=params)

        try:
            data = resp.json()
        except json.JSONDecodeError:
            print('wrong format of data')
        else:
            return (data)
