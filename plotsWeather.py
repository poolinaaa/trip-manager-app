from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import requests
import json
import config as c
from datetime import timedelta, datetime
import csv

class WeatherData():
    
    def __init__(self, countryName, dateFlight='2000-02-02'):
        self.countryName = countryName
        self.dateFlight = dateFlight
    
    def searchCoordinates(self):
        country = self.countryName.get().capitalize()
        with open('worldcities.csv', encoding='utf8') as csvFile:
            csvRead = csv.reader(csvFile, delimiter=',')
            for row in csvRead:
                if row[4] == country:
                    if row[8] == 'primary':
                        lat = row[2]
                        lng = row[3]
                        break
        return lat, lng


    def getWeather(self):
        lat, lng = self.searchCoordinates()
        date = datetime.strptime(self.dateFlight, '%Y-%m-%d').date()
        print(date)
        yearAgo = date - timedelta(days=365)
        print(yearAgo)
        yearAgoPlusMonth = yearAgo + timedelta(days=29)
        print(yearAgoPlusMonth)

        paramsArchive = {'latitude': lat,
                        'longitude': lng,
                        'start_date': yearAgo,
                        'end_date': yearAgoPlusMonth,
                        'daily': 'temperature_2m_mean',
                        'timezone': 'GMT'}

        paramsCurrent = {'latitude': lat,
                        'longitude': lng,
                        'hourly': 'temperature_2m,precipitation_probability,precipitation'}

        urlArchive = 'https://archive-api.open-meteo.com/v1/archive'

        urlCurrent = 'https://api.open-meteo.com/v1/forecast'

        reqArchive = requests.get(url=urlArchive, params=paramsArchive)
        reqCurrent = requests.get(url=urlCurrent, params=paramsCurrent)

        try:
            current = reqCurrent.json()
            archive = reqArchive.json()
            print(current)
            print(archive)
        except json.JSONDecodeError:
            print('error forecast')
        finally:
            return current, archive


class PlotYearAgo():
    
    def __init__(self, countryName, dateFlight):
        self.countryName = countryName
        self.dateFlight = dateFlight
    
    def preparingPastData(self, pastData: dict):
        days = pastData['daily']['time']
        temperature = pastData['daily']['temperature_2m_mean']
        return days, temperature


    def createPlotWeatherYearAgo(self, parent, pastData,pic):
        pic.destroy()
        futureData, pastData = WeatherData(self.countryName, self.dateFlight).getWeather()
        x, y = self.preparingPastData(dict(pastData))
        print(x)
        xFormatted = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in x]
        


        fig = Figure(figsize=(6, 3.2))
        plotPast = fig.add_subplot(111)
        color = 'teal'
        plotPast.plot(xFormatted, y,'-o',color=color)
        
        plotPast.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        
        plotPast.xaxis.set_major_locator(mdates.DayLocator(interval=3))
        plotPast.xaxis.set_minor_locator(mdates.DayLocator())
        plotPast.margins(x=0,y=0.05)
        plotPast.tick_params(axis='x', labelrotation=30, labelsize=7)
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=1, columnspan=2)
        plotPast.tick_params(axis='y', labelsize=7)
        plotPast.set_ylabel('Degrees [°C]',fontsize=8)
        plotPast.set_title('Temperature year ago',fontsize=11)
        fig.tight_layout()

class PlotNextWeek():
    def __init__(self, countryName):
        self.countryName = countryName
    
    def preparingCurrentData(self, futureData: dict):
        time = futureData['hourly']['time']
        temperature = futureData['hourly']['temperature_2m']
        precipitationProb = futureData['hourly']['precipitation_probability']
        precipitation = futureData['hourly']['precipitation']

        return time, temperature, precipitationProb, precipitation


    def createPlotWeatherCurrent(self, parent, futureData,pic):
        pic.destroy()
        futureData, pastData = WeatherData(self.countryName).getWeather()
        x, y, y1, y2 = self.preparingCurrentData(dict(futureData))
        xFormatted = [dt.datetime.strptime(d[:10]+d[11:], '%Y-%m-%d%H:%M') for d in x ]
        
        
        fig, ax1 = plt.subplots(figsize=(6, 3.2))
        color = 'maroon'
        ax1.set_ylabel('Degrees [°C]', color=color, fontsize= 7)
        ax1.plot(xFormatted, y, color=color)
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.tick_params(axis='y', labelsize=5)
        ax1.margins(x=0,y=0.05)
        ax1.tick_params(axis='x', labelrotation=30, labelsize=6)
        ax1.set_title('Weather for the next week',fontsize=11)
        
        ax2 = ax1.twinx()
        color = 'teal'
        ax2.set_ylabel('Precipitation [mm]', color=color, fontsize= 7) 
        ax2.plot(xFormatted, y2, color=color, alpha=0)
        ax2.fill_between(xFormatted,y2,color=color,alpha=0.3)
        ax2.tick_params(axis='y', labelcolor=color)
        ax2.tick_params(axis='y', labelsize=6)
        ax2.margins(x=0,y=0.05)
        
        ax3 = ax1.twinx()
        color = 'rebeccapurple'
        
        ax3.plot(xFormatted, y1, color=color, ls=':')
        ax3.tick_params(axis='y', labelcolor=color)
        ax3.tick_params(axis='y', labelsize=6)
        ax3.set_ylabel('Precipitation probability [%]', color=color, fontsize= 7)
        ax3.margins(x=0,y=0.05)
        ax3.spines['right'].set_position(('outward', 30))
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.gca().xaxis.set_minor_locator(mdates.HourLocator())

        fig.tight_layout()  
        
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=1, columnspan=2)

