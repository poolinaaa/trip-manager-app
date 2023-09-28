import tkinter.font
import requests
import json
import tkinter as tk
import csv
import customtkinter
from base import FrameBase
from PIL import ImageTk
import os

class Frame1(FrameBase):
    '''class of main menu frame'''

    def __init__(self, masterWindow, colorOfBg, colorDetails, colorHighlight, countryName, baseCurrency, codeCurrency):
        super().__init__(masterWindow=masterWindow,
                         colorOfBg=colorOfBg, colorDetails=colorDetails, colorHighlight=colorHighlight, countryName=countryName, baseCurrency=baseCurrency, codeCurrency=codeCurrency)
        self.gen = self.counterFrame1()
        self.masterWindow = masterWindow
        self.load()

    # connect frames with each other
    def setFrames(self, frame1, frame2, frame3, frame4):
        self.frame1 = frame1
        self.frame2 = frame2
        self.frame3 = frame3
        self.frame4 = frame4

    # loading the frame
    def load(self):
        self.tkraise()

        # counter which controls if fake or real button should be packed
        self.nr = next(self.gen)

        # title
        self.labelTitle = tk.Label(master=self, text="Get ready for the journey!",
                                   font=tkinter.font.Font(**self.titleFont), bg=self.colorOfBg, fg='white')

        # fields to enter destination and base currency
        self.frameQuestions = tk.Frame(master=self, width=100,  bg=self.colorOfBg,
                                       highlightbackground=self.colorOfBg, highlightcolor=self.colorOfBg)

        # country
        self.labelCountry = tk.Label(master=self.frameQuestions, text="What country is your destination?",
                                     width=30, font=tkinter.font.Font(**self.questionFont), bg=self.colorOfBg, fg='white', anchor="w")

        self.entryCountry = tk.Entry(master=self.frameQuestions,
                                     width=20, textvariable=self.countryName)

        # base currency
        self.labelBaseCurrency = tk.Label(master=self.frameQuestions, text="What is your base currency?",
                                          width=30, font=tkinter.font.Font(**self.questionFont), bg=self.colorOfBg, fg='white', anchor="w")

        self.entryCurrency = tk.Entry(master=self.frameQuestions,
                                      width=20, textvariable=self.baseCurrency)

        # frame with 3 sections: currency, geography and weather
        self.frameSections = tk.Frame(master=self, width=300, bg=self.colorOfBg,
                                      highlightbackground=self.colorOfBg, highlightcolor=self.colorOfBg)

        # frame currency: create, add title and image
        self.frameCurrency = ThemeSection(
            self.frameSections, self.colorDetails, self.colorHighlight)
        self.frameCurrency.addTitleLabel(title='Changes in currency')
        self.frameCurrency.addImage(os.path.join(os.path.dirname(__file__), 'images', 'cash.png'))

        self.labelCurrentRate = tk.Label(
            master=self.frameCurrency, text='Current rate:', bg=self.colorHighlight, font=tkinter.font.Font(**self.errorFont), fg='white')

        # frame geography: create, add title and image
        self.frameGeography = ThemeSection(
            self.frameSections, self.colorDetails, self.colorHighlight)
        self.frameGeography.addTitleLabel(title='Geographical details')
        self.frameGeography.addImage(os.path.join(os.path.dirname(__file__), 'images', 'plane.png'))

        # frame weather: create, add title and image
        self.frameWeather = ThemeSection(
            self.frameSections, self.colorDetails, self.colorHighlight)
        self.frameWeather.addTitleLabel(title='Check the weather')
        self.frameWeather.addImage(os.path.join(os.path.dirname(__file__), 'images', 'sun.png'))

        # fake buttons (entries to the frames because changing state of customtkinter buttons did not work)
        self.fake1 = customtkinter.CTkButton(master=self.frameCurrency, text='CURRENCY', fg_color=self.colorDetails,
                                             width=20, state=tk.DISABLED)
        self.fake2 = customtkinter.CTkButton(master=self.frameGeography, text='GEOGRAPHY', fg_color=self.colorDetails,
                                             width=20, state=tk.DISABLED)
        self.fake3 = customtkinter.CTkButton(master=self.frameWeather, text='WEATHER', fg_color=self.colorDetails,
                                             width=20, state=tk.DISABLED)

        # real buttons (shown after entering destination)
        self.buttonLoadFrame2 = customtkinter.CTkButton(master=self.frameCurrency, text='CURRENCY', fg_color=self.colorDetails,
                                                        width=20, command=lambda: self.loadFrame(self.frame2))
        self.buttonLoadFrame3 = customtkinter.CTkButton(master=self.frameGeography, text='GEOGRAPHY', fg_color=self.colorDetails,
                                                        width=20, command=lambda: self.multipleFuncButton(self.loadFrame(self.frame3), self.preparingLabelCities(self.frame3.frameCities)))
        self.buttonCountrySearch = customtkinter.CTkButton(master=self.frameQuestions, width=8,
                                                           fg_color=self.colorHighlight, text="SEARCH", command=self.searchButton)
        self.buttonLoadFrame4 = customtkinter.CTkButton(master=self.frameWeather, text='WEATHER', fg_color=self.colorDetails,
                                                        width=20, command=lambda: self.loadFrame(self.frame4))
        # exit whole app button
        self.exitButton = customtkinter.CTkButton(master=self, text='EXIT', fg_color=self.colorDetails,
                                                  width=100, command=self.masterWindow.destroy)
        # PACKING
        # entries, their labels and button search
        self.labelCountry.grid(column=0, row=0, pady=10)
        self.entryCountry.grid(column=1, row=0, pady=10, padx=5)
        self.labelBaseCurrency.grid(column=0, row=2, pady=10)
        self.entryCurrency.grid(column=1, row=2, pady=10, padx=5)
        self.buttonCountrySearch.grid(column=0, row=4, columnspan=2, pady=10)

        # sections
        for nr, frame in enumerate([self.frameCurrency, self.frameGeography, self.frameWeather], start=0):
            frame.grid(column=nr, row=0, sticky='nsew')

        # main parts: title, frames (options and sections)
        for widget in (self.labelTitle, self.frameQuestions, self.labelCurrentRate, self.frameSections):
            widget.pack()

        # buttons of sections
        if self.nr == 1:
            for btn in (self.fake1, self.fake2, self.fake3):
                btn.pack(side=tk.BOTTOM)
        else:
            for btn in (self.buttonLoadFrame2, self.buttonLoadFrame3, self.buttonLoadFrame4):
                btn.pack(side=tk.BOTTOM)

        # button exiting the whole app
        self.exitButton.pack(pady=50)

    # func which is called after clicking the search button
    def searchButton(self):

        # get and format user input
        self.countryToFind = self.countryName.get().capitalize()
        self.base = self.baseCurrency.get().upper()
        self.codeCurrency = self.checkingCurrency().upper()
        self.baseCurrName = self.checkingBase()

        # Display an error message if the entered country name is incorrect
        if self.codeCurrency == 'COUNTRY ERROR':
            countryError = 'You have entered wrong name of country. Please try again (check full name of country)'
            self.errorLabel = tk.Label(
                master=self.frameQuestions, text=countryError, font=tkinter.font.Font(**self.errorFont), bg=self.colorOfBg, fg='white')
            self.errorLabel.grid(column=0, row=1, columnspan=2)
            self.frameQuestions.after(5000, self.errorLabel.destroy)
        else:
            # update elements based on valid input
            self.frameCurrency.title['text'] = f'Analyse changes in {self.codeCurrency}'

            # replacing fake buttons with real ones
            for btn in (self.fake1, self.fake2, self.fake3):
                btn.destroy()

            for btn in (self.buttonLoadFrame2, self.buttonLoadFrame3, self.buttonLoadFrame4):
                btn.pack(side=tk.BOTTOM)

            if self.baseCurrName == self.base or self.baseCurrName == 'EUR':
                # retrieve current currency exchange rate data using an API

                headers = {"apikey": "uk5pSwPkDIdeHqRIJbOTBWjr9YT3T73E"}
                params = {'from': self.codeCurrency,
                          'to' : self.baseCurrName,
                          
                          'base': self.codeCurrency}
                r = requests.get(
                    'https://api.apilayer.com/fixer/latest', params=params, headers=headers)
                try:
                    data = r.json()
                    print(data)
                except json.JSONDecodeError:
                    print('Wrong format of data.')
                else:

                    self.currentRate = data["rates"][self.baseCurrName]
                    self.labelCurrentRate['text'] = f'Current rate: {self.currentRate} {self.baseCurrName}'

    def preparingLabelCities(self, frame):
        # retrieve geographical information about the destination country (it will be used in the frame3 (geography section))
        self.destinationGeoInfo = self.searchInfoAboutDestination()

        self.frame3.labelTitle[
            'text'] = f'Discover some geographical facts about {self.countryName.get().capitalize()}'

        capital = self.destinationGeoInfo.get('capital', 'No capital found')
        cities = [city for city in self.destinationGeoInfo['citiesPopulation']]
        population = [self.destinationGeoInfo['citiesPopulation'][city]
                      for city in self.destinationGeoInfo['citiesPopulation']]

        # create labels with geographical information (the biggest cities with population)
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
        # retrieve information about the destination country from a CSV file

        country = self.countryName.get().capitalize()
        self.fiveCitiesExamples = dict()
        cnt = 0
        self.dictInfo = dict()

        with open('worldcities.csv', encoding='utf8') as csvFile:
            csvRead = csv.reader(csvFile, delimiter=',')
            for row in csvRead:
                if row[4] == country:
                    self.dictInfo['iso'] = row[5]
                    # saving 5 the biggest cities with population
                    if cnt < 5:
                        self.fiveCitiesExamples[row[1]] = row[9]
                        cnt += 1
                    if row[8] == 'primary':
                        # saving latitude and longitude of the capital
                        self.dictInfo['capital'] = row[1]
                        self.dictInfo['lat'] = row[2]
                        self.dictInfo['lng'] = row[3]
            self.dictInfo['citiesPopulation'] = self.fiveCitiesExamples
        return self.dictInfo

    def checkingCurrency(self):
        # checking what currency is used in a given country

        with open('countryCurrency.csv') as csvFile:
            currencyCode = 'code'
            csvRead = csv.reader(csvFile, delimiter=',')
            for row in csvRead:
                if row[0] == self.countryToFind:
                    currencyCode = row[3]
            if currencyCode == 'code':
                # returning error (unavailable data or spelling error country)
                return 'COUNTRY ERROR'
            else:
                # returning currency code which is used in destination country
                return currencyCode

    def checkingBase(self):
        # checking if entered currency code is correct

        with open('countryCurrency.csv') as csvFile:
            csvRead = csv.reader(csvFile, delimiter=',')
            for row in csvRead:
                if row[3] == self.base:
                    result = self.base
                    print(result)
                    print('evr ok')
                    return result

            if 'result' not in locals():
                # notification about default base currency (EUR)

                self.errorBaseLabel = tk.Label(
                    master=self.frameQuestions, text='BaseCurrencyError: correct base currency name, current base is set default (EUR)',
                    font=tkinter.font.Font(**self.errorFont), bg=self.colorOfBg, fg='white')
                self.errorBaseLabel.grid(column=0, row=3, columnspan=2)
                self.frameQuestions.after(5000, self.errorBaseLabel.destroy)

                return 'EUR'

    @staticmethod
    def counterFrame1():
        # generator checking if fake or real buttons should be packed
        i = 1
        while True:
            yield i
            i += 1


class ThemeSection(tk.Frame):
    '''class of sections: currency, geography and weather'''

    def __init__(self, masterFrame, colorDetails, colorHighlight, **kwargs):
        super().__init__(master=masterFrame, bg=colorHighlight,
                         **kwargs)
        self.headingF = tkinter.font.Font(family="Lato", size=11)
        self.textF = tkinter.font.Font(family="Lato", size=8)
        self.colorDetails = colorDetails
        self.colorHighlight = colorHighlight

    def addTitleLabel(self, title: str):
        '''set the title of the section'''
        self.title = tk.Label(
            self, text=title, width=30, font=self.headingF, bg=self.colorDetails, fg='white')
        self.title.pack(pady=10)

    def addImage(self, nameOfFile):
        '''adding image connected with theme of section'''
        self.pictureSection = ImageTk.PhotoImage(file=nameOfFile)
        self.pictureWidget = tk.Label(
            master=self, image=self.pictureSection, bg=self.colorDetails, width=100, height=100)
        self.pictureWidget.image = self.pictureSection
        self.pictureWidget.pack(pady=10)
