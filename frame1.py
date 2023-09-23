import tkinter.font
import requests
import json
import tkinter as tk
import csv
import customtkinter
from base import FrameBase
from PIL import ImageTk


class Frame1(FrameBase):

    def __init__(self, masterWindow, colorOfBg, colorDetails, colorHighlight, countryName, baseCurrency, codeCurrency):
        super().__init__(masterWindow=masterWindow,
                         colorOfBg=colorOfBg, colorDetails=colorDetails, colorHighlight=colorHighlight, countryName=countryName, baseCurrency=baseCurrency, codeCurrency=codeCurrency)
        self.gen = self.counterFrame1()
        self.masterWindow = masterWindow
        self.load()

    def setFrames(self, frame1, frame2, frame3, frame4):
        self.frame1 = frame1
        self.frame2 = frame2
        self.frame3 = frame3
        self.frame4 = frame4

    def load(self):
        self.tkraise()
        self.nr = next(self.gen)

        # title
        self.labelTitle = tk.Label(master=self, text="Let's prepare for your trip!",
                                   font=tkinter.font.Font(**self.titleFont), bg=self.colorOfBg, fg='white')

        # fields to enter destination and base currency
        self.frameQuestions = tk.Frame(master=self, width=100,  bg=self.colorOfBg,
                                       highlightbackground=self.colorOfBg, highlightcolor=self.colorOfBg)

        self.labelCountry = tk.Label(master=self.frameQuestions, text="What country is your destination?",
                                     width=30, font=tkinter.font.Font(**self.questionFont), bg=self.colorOfBg, fg='white', anchor="w")

        self.entryCountry = tk.Entry(master=self.frameQuestions,
                                     width=20, textvariable=self.countryName)

        self.labelBaseCurrency = tk.Label(master=self.frameQuestions, text="What is your base currency?",
                                          width=30, font=tkinter.font.Font(**self.questionFont), bg=self.colorOfBg, fg='white', anchor="w")

        self.entryCurrency = tk.Entry(master=self.frameQuestions,
                                      width=20, textvariable=self.baseCurrency)

        self.frameSections = tk.Frame(master=self, width=300, bg=self.colorOfBg,
                                      highlightbackground=self.colorOfBg, highlightcolor=self.colorOfBg)

        self.frameCurrency = ThemeSection(
            self.frameSections, self.colorDetails, self.colorHighlight)
        self.frameCurrency.addTitleLabel(title='Changes in currency')

        self.frameCurrency.addImage('cash.png')

        self.labelCurrentRate = tk.Label(
            master=self.frameCurrency, text='Current rate:', bg=self.colorHighlight, font=tkinter.font.Font(**self.errorFont), fg='white')

        # flights
        self.frameFlights = ThemeSection(
            self.frameSections, self.colorDetails, self.colorHighlight)
        self.frameFlights.addTitleLabel(title='Geographical details')

        self.frameFlights.addImage('plane.png')

        # weather
        self.frameWeather = ThemeSection(
            self.frameSections, self.colorDetails, self.colorHighlight)
        self.frameWeather.addTitleLabel(title='Check the weather')

        self.frameWeather.addImage('sun.png')

        # fake buttons (entries to the frames because changing state of customtkinter buttons did not work)
        self.fake1 = customtkinter.CTkButton(master=self.frameCurrency, text='CURRENCY', fg_color=self.colorDetails,
                                             width=20, state=tk.DISABLED)
        self.fake2 = customtkinter.CTkButton(master=self.frameFlights, text='GEOGRAPHY', fg_color=self.colorDetails,
                                             width=20, state=tk.DISABLED)
        self.fake3 = customtkinter.CTkButton(master=self.frameWeather, text='WEATHER', fg_color=self.colorDetails,
                                             width=20, state=tk.DISABLED)

        # real buttons (shown after entering destination)
        self.buttonLoadFrame2 = customtkinter.CTkButton(master=self.frameCurrency, text='CURRENCY', fg_color=self.colorDetails,
                                                        width=20, command=lambda: self.loadFrame(self.frame2))
        self.buttonLoadFrame3 = customtkinter.CTkButton(master=self.frameFlights, text='GEOGRAPHY', fg_color=self.colorDetails,
                                                        width=20, command=lambda: self.multipleFuncButton(self.loadFrame(self.frame3), self.preparingLabelCities(self.frame3.frameCities)))
        self.buttonCountrySearch = customtkinter.CTkButton(master=self.frameQuestions, width=8,
                                                           fg_color=self.colorHighlight, text="SEARCH", command=self.searchButton)
        self.buttonLoadFrame4 = customtkinter.CTkButton(master=self.frameWeather, text='WEATHER', fg_color=self.colorDetails,
                                                        width=20, command=lambda: self.loadFrame(self.frame4))
        
        self.exitButton = customtkinter.CTkButton(master=self, text='EXIT', fg_color=self.colorDetails,
                                                        width=100, command=self.masterWindow.destroy) 
        # PACKING
        self.labelCountry.grid(column=0, row=0, pady=10)
        self.entryCountry.grid(column=1, row=0, pady=10, padx=5)
        self.labelBaseCurrency.grid(column=0, row=2, pady=10)
        self.entryCurrency.grid(column=1, row=2, pady=10, padx=5)
        self.frameCurrency.grid(column=0, row=0, sticky='nsew')
        self.frameFlights.grid(column=1, row=0, sticky='nsew')
        self.frameWeather.grid(column=2, row=0, sticky='nsew')

        self.buttonCountrySearch.grid(column=0, row=3, columnspan=2, pady=10)

        for widget in (self.labelTitle, self.frameQuestions, self.labelCurrentRate, self.frameSections):
            widget.pack()

        if self.nr == 1:
            for btn in (self.fake1, self.fake2, self.fake3):
                btn.pack(side=tk.BOTTOM)

        else:
            for btn in (self.buttonLoadFrame2, self.buttonLoadFrame3, self.buttonLoadFrame4):
                btn.pack(side=tk.BOTTOM)
                
        self.exitButton.pack(pady=50)

    def searchButton(self):

        self.countryToFind = self.countryName.get().capitalize()

        self.base = self.baseCurrency.get().upper()

        self.codeCurrency = self.checkingCurrency().upper()
        self.baseCurrName = self.checkingBase()

        if self.codeCurrency == 'COUNTRY ERROR':
            countryError = 'You have entered wrong name of country. Please try again (check full name of country)'
            self.errorLabel = tk.Label(
                master=self.frameQuestions, text=countryError, font=tkinter.font.Font(**self.errorFont), bg=self.colorOfBg, fg='white')
            self.errorLabel.grid(column=0, row=1, columnspan=2)
            self.frameQuestions.after(5000, self.errorLabel.destroy)
        else:
            self.frameCurrency.title['text'] = f'Analyse changes in {self.codeCurrency}'

            self.fake1.destroy()
            self.fake2.destroy()
            self.fake3.destroy()
            self.buttonLoadFrame2.pack(side=tk.BOTTOM)

            self.buttonLoadFrame3.pack(side=tk.BOTTOM)

            self.buttonLoadFrame4.pack(side=tk.BOTTOM)
            print(self.baseCurrName)
            print(self.base)
            

            
            
            if self.baseCurrName == self.base or self.baseCurrName == 'EUR':
                
                headers= {
                "apikey": "uk5pSwPkDIdeHqRIJbOTBWjr9YT3T73E"
                }
                params = {'from': self.baseCurrName,
                          'amount':'1',
                          'to': self.codeCurrency}
                r = requests.get(
                    'https://api.apilayer.com/fixer/latest', params=params, headers=headers)
                try:
                    data = r.json()
                except json.JSONDecodeError:
                    print('Wrong format of data.')
                else:
                    print(data)
                    self.currentRate = data["rates"][self.codeCurrency]

                    self.labelCurrentRate['text'] = f'Current rate: {self.currentRate} {self.baseCurrName}'

    def preparingLabelCities(self, frame):
        self.destinationGeoInfo = self.searchInfoAboutDestination()
        print(self.destinationGeoInfo)
        self.frame3.labelTitle[
            'text'] = f'Discover some geographical facts about {self.countryName.get().capitalize()}'

        capital = self.destinationGeoInfo.get('capital', 'No capital found')
        cities = [city for city in self.destinationGeoInfo['citiesPopulation']]
        population = [self.destinationGeoInfo['citiesPopulation'][city]
                      for city in self.destinationGeoInfo['citiesPopulation']]
        print(cities)
        print(capital)
        print(population)

        self.labelCapital = tk.Label(
            frame, text=f'Capital: {capital}', font=tkinter.font.Font(**self.questionFont), bg=self.colorDetails, fg='white')
        if len(cities) >= 5 and len(population) >= 5:
            self.labelCities = tk.Label(
                frame, text=f'''The most crowded cities:
                \n{cities[0]}, population: {population[0]}
                \n{cities[1]}, population: {population[1]}
                \n{cities[2]}, population: {population[2]}
                \n{cities[3]}, population: {population[3]}
                \n{cities[4]}, population: {population[4]}''', font=tkinter.font.Font(**self.questionFont), bg=self.colorHighlight, fg='white', justify='left')
        else:

            self.labelCities = tk.Label(
                frame, text="Not enough data available for cities.", font=tkinter.font.Font(**self.questionFont), bg=self.colorHighlight, fg='white')
        self.labelCapital.grid(column=0, row=0, pady=10, padx=30, sticky='ew')
        self.labelCities.grid(column=0, row=1, pady=10, padx=30)

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

    def checkingCurrency(self):
        with open('countryCurrency.csv') as csvFile:
            csvRead = csv.reader(csvFile, delimiter=',')
            for row in csvRead:
                if row[0] == self.countryToFind:
                    currencyCode = row[3]
            if 'currencyCode' not in locals():
                labelErr = tk.Label(self.frameCurrency, text='')
                return 'COUNTRY ERROR'
            else:
                return currencyCode

    def checkingBase(self):
        with open('countryCurrency.csv') as csvFile:
            csvRead = csv.reader(csvFile, delimiter=',')
            for row in csvRead:
                if row[3] == self.base:
                    result = self.base
                    print(result)
                    print('evr ok')
                    return result
            if 'result' not in locals():
                print(
                    'BaseCurrencyError: correct base currency name, current base is set default (EUR)')
                return 'EUR'

    @staticmethod
    def counterFrame1():
        i = 1
        while True:
            yield i
            i += 1


class ThemeSection(tk.Frame):

    def __init__(self, masterFrame, colorDetails, colorHighlight, **kwargs):
        super().__init__(master=masterFrame, bg=colorHighlight,
                         **kwargs)
        self.headingF = tkinter.font.Font(family="Lato", size=11)
        self.textF = tkinter.font.Font(family="Lato", size=8)
        self.colorDetails = colorDetails
        self.colorHighlight = colorHighlight

    def addTitleLabel(self, title: str):
        self.title = tk.Label(
            self, text=title, width=30, font=self.headingF, bg=self.colorDetails, fg='white')
        self.title.pack(pady=10)

    def addImage(self, nameOfFile):
        self.pictureSection = ImageTk.PhotoImage(file=nameOfFile)
        self.pictureWidget = tk.Label(
            master=self, image=self.pictureSection, bg=self.colorDetails, width=100, height=100)
        self.pictureWidget.image = self.pictureSection
        self.pictureWidget.pack(pady=10)
