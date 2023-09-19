import tkinter.font
import requests
import json
import tkinter as tk
from currencyFunc import checkingCurrency, checkingBase
from funcBehaviorFrames import appearance,  multipleFuncButton
import config as c
from tkcalendar import *
from tkinter import *
import requests
import json
import tkinter as tk
from tkinter import *
from sqlite3 import *
import csv
import customtkinter
from base import FrameBase
from PIL import ImageTk
import tkinter as tk
import tkinter.font
from funcBehaviorFrames import appearance
appearance()


class Frame1(FrameBase):

    def __init__(self, masterWindow, colorOfBg, countryName, baseCurrency):
        super().__init__(masterWindow=masterWindow,
                         colorOfBg=colorOfBg, countryName=countryName, baseCurrency=baseCurrency)
        self.gen = self.counterFrame1()
        self.errorLabel = None
        self.colorOfBg = colorOfBg
        self.load()

    def setFrames(self, frame1, frame2, frame3, frame4):
        self.frame1 = frame1
        self.frame2 = frame2
        self.frame3 = frame3
        self.frame4 = frame4

    def load(self):
        self.tkraise()
        nr = next(self.gen)

        # title
        self.labelTitle = tk.Label(master=self, text="Let's prepare for your trip!",
                                   font=c.titleFont, bg=self.colorOfBg, fg='white')

        # fields to enter destination and base currency
        self.frameQuestions = tk.Frame(master=self, width=100,  bg=self.colorOfBg,
                                       highlightbackground=self.colorOfBg, highlightcolor=self.colorOfBg)

        self.labelCountry = tk.Label(master=self.frameQuestions, text="What country is your destination?",
                                     width=30, font=c.questionFont, bg=self.colorOfBg, fg='white', anchor="w")
        self.labelCountry.grid(column=0, row=0, pady=10)

        self.entryCountry = tk.Entry(master=self.frameQuestions,
                                     width=20, textvariable=self.countryName)
        self.entryCountry.grid(column=1, row=0, pady=10, padx=5)

        self.labelBaseCurrency = tk.Label(master=self.frameQuestions, text="What is your base currency?",
                                          width=30, font=c.questionFont, bg=self.colorOfBg, fg='white', anchor="w")
        self.labelBaseCurrency.grid(column=0, row=2, pady=10)

        self.entryCurrency = tk.Entry(master=self.frameQuestions,
                                      width=20, textvariable=self.baseCurrency)
        self.entryCurrency.grid(column=1, row=2, pady=10, padx=5)

        self.frameSections = tk.Frame(master=self, width=300, bg=self.colorOfBg,
                                      highlightbackground=self.colorOfBg, highlightcolor=self.colorOfBg)

        self.frameCurrency = ThemeSection(self.frameSections)
        self.frameCurrency.addTitleLabel(title='Changes in currency')
        self.frameCurrency.grid(column=0, row=0, sticky='nsew')
        self.frameCurrency.addImage('cash.png')

        self.labelCurrentRate = tk.Label(
            master=self.frameCurrency, text='Current rate:', bg=c.highlight, font=c.errorFont, fg='white')

        # flights
        self.frameFlights = ThemeSection(self.frameSections)
        self.frameFlights.addTitleLabel(title='Geographical details')
        self.frameFlights.grid(column=1, row=0, sticky='nsew')
        self.frameFlights.addImage('plane.png')

        # weather
        self.frameWeather = ThemeSection(self.frameSections)
        self.frameWeather.addTitleLabel(title='Check the weather')
        self.frameWeather.grid(column=2, row=0, sticky='nsew')
        self.frameWeather.addImage('sun.png')

        self.fake1 = customtkinter.CTkButton(master=self.frameCurrency, text='CURRENCY', fg_color=c.details,
                                             width=20, state=tk.DISABLED)
        self.fake2 = customtkinter.CTkButton(master=self.frameFlights, text='GEOGRAPHY', fg_color=c.details,
                                             width=20, state=tk.DISABLED)
        self.fake3 = customtkinter.CTkButton(master=self.frameWeather, text='WEATHER', fg_color=c.details,
                                             width=20, state=tk.DISABLED)

        self.buttonLoadFrame2 = customtkinter.CTkButton(master=self.frameCurrency, text='CURRENCY', fg_color=c.details,
                                                        width=20, command=lambda: self.loadFrame(self.frame2))
        self.buttonLoadFrame3 = customtkinter.CTkButton(master=self.frameFlights, text='GEOGRAPHY', fg_color=c.details,
                                                        width=20, command=lambda: self.multipleFuncButton(self.loadFrame(self.frame3), self.preparingLabelCities(self.frame3.frameCities)))
        self.buttonCountrySearch = customtkinter.CTkButton(
            master=self.frameQuestions, width=8, fg_color=c.highlight, text="SEARCH", command=self.searchButton)
        self.buttonLoadFrame4 = customtkinter.CTkButton(master=self.frameWeather, text='WEATHER', fg_color=c.details,
                                                        width=20, command=lambda: self.loadFrame(self.frame4))
        
        
        
        
        
        self.buttonCountrySearch.grid(column=0, row=3, columnspan=2, pady=10)

        for widget in (self.labelTitle, self.frameQuestions, self.labelCurrentRate, self.frameSections):
            widget.pack()

        if nr == 1:
            for btn in (self.fake1,self.fake2,self.fake3):
                btn.pack(side=tk.BOTTOM)

        else:
            for btn in (self.buttonLoadFrame2,self.buttonLoadFrame3,self.buttonLoadFrame4):
                btn.pack(side=tk.BOTTOM)
            
    def searchButton(self):
        countryToFind = self.countryName.get().capitalize()
        global codeCurrency, baseCurrName
        baseCurrName = self.baseCurrency.get().upper()
        codeCurrency = checkingCurrency(countryToFind).upper()
        baseCurrName = checkingBase(baseCurrName)

        if codeCurrency == 'COUNTRY ERROR':
            countryError = 'You have entered wrong name of country. Please try again (check full name of country)'
            self.errorLabel = tk.Label(
                master=self.frameQuestions, text=countryError, font=c.errorFont, bg=self.colorOfBg, fg='white')
            self.errorLabel.grid(column=0, row=1, columnspan=2)
            self.frameQuestions.after(5000, self.errorLabel.destroy)
        else:
            self.frameCurrency.title['text'] = f'Analyse changes in {codeCurrency}'
            
            self.fake1.destroy()
            self.fake2.destroy()
            self.fake3.destroy()
            self.buttonLoadFrame2.pack(side=tk.BOTTOM)

            self.buttonLoadFrame3.pack(side=tk.BOTTOM)

            self.buttonLoadFrame4.pack(side=tk.BOTTOM)

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
                    self.labelCurrentRate['text'] = f'Current rate: {c.current} {baseCurrName}'
                    
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
    
    @staticmethod
    def counterFrame1():
        i = 1
        while True:
            yield i
            i += 1
    
    
class ThemeSection(tk.Frame):

    def __init__(self, masterFrame, **kwargs):
        super().__init__(master=masterFrame, bg=c.highlight, 
                          **kwargs)
        self.headingF = tkinter.font.Font(family="Lato", size=11)
        self.textF = tkinter.font.Font(family="Lato", size=8)
        

    def addTitleLabel(self, title: str):
        self.title = tk.Label(
            self, text=title, width=30,font=self.headingF, bg=c.details, fg='white')
        self.title.pack(pady=10)

    def addImage(self, nameOfFile):
        self.pictureSection = ImageTk.PhotoImage(file=nameOfFile)
        self.pictureWidget = tk.Label(
            master=self, image=self.pictureSection, bg=c.details, width=100, height=100)
        self.pictureWidget.image = self.pictureSection
        self.pictureWidget.pack(pady=10)