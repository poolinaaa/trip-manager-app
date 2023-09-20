import tkinter as tk
from funcBehaviorFrames import  savingLandmarks
import config as c
from tkcalendar import *
import customtkinter
from tkinter import *
from PIL import ImageTk
import config as c
import tkinter as tk
from tkinter import *
from sqlite3 import *
import csv
from geoFunc import getDistanceBetweenPoints, searchAttractions
import customtkinter
import PIL.Image
from base import FrameBase
import webbrowser
import customtkinter
import tkinter.font
from datetime import datetime

class Frame3(FrameBase):

    def __init__(self, masterWindow, colorOfBg, frame1, countryName, baseCurrency):
        super().__init__(masterWindow=masterWindow,
                         colorOfBg=colorOfBg, countryName=countryName, baseCurrency=baseCurrency)

        self.frame1 = frame1
        self.colorOfBg = colorOfBg
        self.load()

    def load(self):
        self.tkraise()
        self.frameOptions = tk.Frame(self, bg=c.highlight)
        self.backButton = customtkinter.CTkButton(master=self, text='BACK', fg_color=c.details, width=40, height=40,
                                                  command=lambda: self.loadFrame(self.frame1))
        self.backButton.pack(side=TOP, anchor=NW)

        self.labelTitle = tk.Label(master=self, text=f"Discover some geographical facts about {self.countryName.get().capitalize()}",
                                   font=tkinter.font.Font(**self.titleFont), bg=self.colorOfBg, fg='white')
        self.labelTitle.pack()
        self.frameOptions.pack(anchor='e')

        self.labelDepartureCountry = tk.Label(master=self.frameOptions, text="What is your departure country?",
                                              width=30, font=c.questionFont, bg=self.colorOfBg, fg='white', anchor="w")
        self.labelDepartureCountry.grid(column=0, row=0)

        self.departureCountry = tk.StringVar(value='country')

        self.entryDepartureCountry = tk.Entry(
            master=self.frameOptions, textvariable=self.departureCountry)
        self.entryDepartureCountry.grid(column=0, row=1)

        self.labelUnit = tk.Label(master=self.frameOptions, text='Select the unit in which the distance will be displayed',
                                  font=c.questionFont, bg=self.colorOfBg, fg='white', anchor="w")
        self.labelUnit.grid(column=1, row=0, columnspan=2)

        var = tk.StringVar(value='kilometers')

        self.kmButton = tk.Radiobutton(
            master=self.frameOptions, text='kilometers', variable=var, value='kilometers', bg='#9dc0d1')
        self.milesButton = tk.Radiobutton(
            master=self.frameOptions, text='miles', variable=var, value='miles', bg='#9dc0d1')

        self.kmButton.grid(column=1, row=1, pady=5)
        self.milesButton.grid(column=2, row=1, pady=5)

        self.frameCities = tk.Frame(self, bg=c.highlight, height=450)
        self.frameCities.pack(side=LEFT, anchor='n', padx=55, pady=10)
        self.preparingLabelCities(self.frameCities)
        self.frameCheckbutton = tk.Frame(
            master=self, bg='#9dc0d1', width=300, height=450)

        img = (PIL.Image.open("globe.png"))

        resized_image = img.resize((300, 300))
        new_image = ImageTk.PhotoImage(resized_image)

        self.pictureWidget = tk.Label(
            master=self.frameCheckbutton, image=new_image, width=300, height=300, bg=self.colorOfBg)

        self.pictureWidget.image = new_image
        self.pictureWidget.pack()

        self.frameCheckbutton.pack(side=LEFT, pady=30, anchor='n')

        self.buttonConfirmCountry = customtkinter.CTkButton(master=self.frameOptions, text='CONFIRM COUNTRY', fg_color=c.details,
                                                            command=lambda: self.confirmCountry(self.departureCountry, self.frameCheckbutton, var.get()))
        self.buttonConfirmCountry.grid(row=2, column=0, columnspan=3, pady=20)

    def preparingLabelCities(self, frame):
        self.destinationGeoInfo = self.searchInfoAboutDestination()
        print(self.destinationGeoInfo)

        capital = self.destinationGeoInfo.get('capital', 'No capital found')
        cities = [city for city in self.destinationGeoInfo['citiesPopulation']]
        population = [self.destinationGeoInfo['citiesPopulation'][city]
                      for city in self.destinationGeoInfo['citiesPopulation']]
        print(cities)
        print(capital)
        print(population)

        self.labelCapital = tk.Label(
            frame, text=f'Capital: {capital}', font=c.questionFont, bg=c.details, fg='white')
        if len(cities) >= 5 and len(population) >= 5:
            self.labelCities = tk.Label(
                frame, text=f'''The most crowded cities:
                \n{cities[0]}, population: {population[0]}
                \n{cities[1]}, population: {population[1]}
                \n{cities[2]}, population: {population[2]}
                \n{cities[3]}, population: {population[3]}
                \n{cities[4]}, population: {population[4]}''', font=c.questionFont, bg=c.highlight, fg='white', justify='left')
        else:
            # Obsłuż sytuację, gdy lista nie ma wystarczającej liczby elementów
            self.labelCities = tk.Label(
                frame, text="Not enough data available for cities.", font=c.questionFont, bg=c.highlight, fg='white')
        self.labelCapital.pack(pady=10, padx=30)
        self.labelCities.pack(pady=10, padx=30)

    def searchInfoAboutDestination(self):
        country = self.countryName.get().capitalize()
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

    def confirmCountry(self, strVarCountry, frame, unit):
        for widget in frame.winfo_children():
            widget.destroy()
        baseCountry = strVarCountry.get().capitalize()
        baseCountry = self.checkingCountry(baseCountry)

        with open('worldcities.csv', encoding='utf8') as csvFile:
            csvRead = csv.reader(csvFile, delimiter=',')
            for row in csvRead:
                if row[4] == baseCountry:
                    isoBase = row[5]
                    latBase = row[2]
                    lngBase = row[3]
                    break

            destinationGeoInfo = self.searchInfoAboutDestination()
            print(destinationGeoInfo)

            distance = getDistanceBetweenPoints(
                latBase, lngBase, destinationGeoInfo['lat'], destinationGeoInfo['lng'], unit)

            distanceLabel = tk.Label(
                master=frame, text=f'Distance between {baseCountry} and {self.countryName.get().capitalize()} is about \n{distance} {unit}', font=c.questionFont, bg=c.highlight, fg='white', anchor="w")
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

    def checkingCountry(self, country):
        with open('countries.csv', encoding='utf8') as csvFile:
            csvRead = csv.reader(csvFile, delimiter=',')
            for row in csvRead:
                if row[2] == country:
                    foundCountry = row[2]

            if 'foundCountry' not in locals():
                return 'CountryError'
            else:
                return foundCountry
            
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