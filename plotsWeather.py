from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import requests
import json
from datetime import timedelta, datetime
import csv


class WeatherData():
    '''class WeatherData for retrieving weather information'''

    def __init__(self, countryName, dateDeparture='2000-02-02'):
        self.countryName = countryName
        self.dateDeparture = dateDeparture

    # check longitude and latitude of capital (of chosen destination)
    def searchCoordinates(self):
        country = self.countryName.get().capitalize()
        with open('worldcities.csv', encoding='utf8') as csvFile:
            lat = None
            lng = None
            csvRead = csv.reader(csvFile, delimiter=',')
            for row in csvRead:
                if row[4] == country:
                    if row[8] == 'primary':
                        lat = row[2]
                        lng = row[3]
                        break
        return lat, lng

    # get weather data for the specified location and date (using API)
    def getWeather(self):
        current = dict()
        archive = dict()
        lat, lng = self.searchCoordinates()
        date = datetime.strptime(self.dateDeparture, '%Y-%m-%d').date()

        # get month year ago
        yearAgo = date - timedelta(days=365)
        yearAgoPlusMonth = yearAgo + timedelta(days=29)

        #params for getting data for year ago
        paramsArchive = {'latitude': lat,
                         'longitude': lng,
                         'start_date': yearAgo,
                         'end_date': yearAgoPlusMonth,
                         'daily': 'temperature_2m_mean',
                         'timezone': 'GMT'}
        
        #params for getting data for the next week
        paramsCurrent = {'latitude': lat,
                         'longitude': lng,
                         'hourly': 'temperature_2m,precipitation_probability,precipitation'}

        #urls and requests
        urlArchive = 'https://archive-api.open-meteo.com/v1/archive'
        urlCurrent = 'https://api.open-meteo.com/v1/forecast'
        reqArchive = requests.get(url=urlArchive, params=paramsArchive)
        reqCurrent = requests.get(url=urlCurrent, params=paramsCurrent)

        try:
            current = reqCurrent.json()
            archive = reqArchive.json()

        except json.JSONDecodeError:
            print('error forecast')
        finally:
            return current, archive


class PlotYearAgo():
    '''class PlotYearAgo for creating weather plots for a year ago'''

    def __init__(self, countryName, dateDeparture):
        self.countryName = countryName
        self.dateDeparture = dateDeparture

    # get dates and temperature
    def preparingPastData(self, pastData: dict):
        days = pastData['daily']['time']
        temperature = pastData['daily']['temperature_2m_mean']
        return days, temperature

    # create a plot for past weather data
    def createPlotWeatherYearAgo(self, parent, pastData, pic):
        
        # destroy picture (which will be replaced with the plot)
        pic.destroy()

        #get and format data
        futureData, pastData = WeatherData(
            self.countryName, self.dateDeparture).getWeather()
        x, y = self.preparingPastData(dict(pastData))
        xFormatted = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in x]

        fig = Figure(figsize=(6, 3.2))
        
        #create axes (temperature year ago)
        plotPast = fig.add_subplot(111)
        color = 'teal'
        plotPast.plot(xFormatted, y, '-o', color=color)
        plotPast.margins(x=0, y=0.05)
        plotPast.tick_params(axis='x', labelrotation=30, labelsize=7)
        plotPast.tick_params(axis='y', labelsize=7)
        plotPast.set_ylabel('Degrees [°C]', fontsize=8)
        plotPast.set_title('Temperature year ago', fontsize=11)
        
        # date labels format
        plotPast.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plotPast.xaxis.set_major_locator(mdates.DayLocator(interval=3))
        plotPast.xaxis.set_minor_locator(mdates.DayLocator())
        
        #place the plot
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=1, columnspan=2)
        


class PlotNextWeek():
    '''class for creating weather plots for the next week from now'''

    def __init__(self, countryName):
        self.countryName = countryName

    # get dates, temperature, sum and probability of precipitation
    def preparingCurrentData(self, futureData: dict):
        time = futureData['hourly']['time']
        temperature = futureData['hourly']['temperature_2m']
        precipitationProb = futureData['hourly']['precipitation_probability']
        precipitation = futureData['hourly']['precipitation']

        return time, temperature, precipitationProb, precipitation

    # create a plot for next week weather data
    def createPlotWeatherCurrent(self, parent, futureData, pic):
        # destroy picture (which will be replaced with the plot)
        pic.destroy()

        # get and format data
        futureData, pastData = WeatherData(self.countryName).getWeather()
        x, y, y1, y2 = self.preparingCurrentData(dict(futureData))
        xFormatted = [dt.datetime.strptime(
            d[:10]+d[11:], '%Y-%m-%d%H:%M') for d in x]

        fig, ax1 = plt.subplots(figsize=(6, 3.2))

        # temperature axes
        color = 'maroon'
        ax1.set_ylabel('Degrees [°C]', color=color, fontsize=7)
        ax1.plot(xFormatted, y, color=color)
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.tick_params(axis='y', labelsize=5)
        ax1.margins(x=0, y=0.05)
        ax1.tick_params(axis='x', labelrotation=30, labelsize=6)
        ax1.set_title('Weather for the next week', fontsize=11)

        # precipitation axes
        ax2 = ax1.twinx()
        color = 'teal'
        ax2.set_ylabel('Precipitation [mm]', color=color, fontsize=7)
        ax2.plot(xFormatted, y2, color=color, alpha=0)
        ax2.fill_between(xFormatted, y2, color=color, alpha=0.3)
        ax2.tick_params(axis='y', labelcolor=color)
        ax2.tick_params(axis='y', labelsize=6)
        ax2.margins(x=0, y=0.05)

        # probability axes
        ax3 = ax1.twinx()
        color = 'rebeccapurple'
        ax3.plot(xFormatted, y1, color=color, ls=':')
        ax3.tick_params(axis='y', labelcolor=color)
        ax3.tick_params(axis='y', labelsize=6)
        ax3.set_ylabel(
            'Precipitation probability [%]', color=color, fontsize=7)
        ax3.margins(x=0, y=0.05)
        ax3.spines['right'].set_position(('outward', 40))

        # date labels format
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.gca().xaxis.set_minor_locator(mdates.HourLocator())

        # placing the graph
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=1, columnspan=2)
