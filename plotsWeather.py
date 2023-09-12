from weather import getWeather
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt


def preparingPastData(pastData: dict):
    days = pastData['daily']['time']
    temperature = pastData['daily']['temperature_2m_mean']
    return days, temperature


def createPlotWeatherYearAgo(parent, pastData):
    futureData, pastData = getWeather()
    x, y = preparingPastData(dict(pastData))
    print(x)
    xFormatted = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in x]
    


    fig = Figure(figsize=(5, 3))
    plotPast = fig.add_subplot(111)
    
    plotPast.plot(xFormatted, y)
    plotPast.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    
    plotPast.xaxis.set_major_locator(mdates.DayLocator(interval=3))
    plotPast.xaxis.set_minor_locator(mdates.DayLocator())
    plotPast.margins(x=0,y=0.05)
    plotPast.tick_params(axis='x', labelrotation=30, labelsize=7)
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=1, columnspan=2)
    plotPast.tick_params(axis='y', labelsize=7)
    plotPast.set_ylabel('Degrees (Celsius scale)')
    plotPast.set_title('Temperature year ago')
    fig.tight_layout()


def preparingCurrentData(futureData: dict):
    time = futureData['hourly']['time']
    temperature = futureData['hourly']['temperature_2m']
    precipitationProb = futureData['hourly']['precipitation_probability']
    precipitation = futureData['hourly']['precipitation']

    return time, temperature, precipitationProb, precipitation


def createPlotWeatherCurrent(parent, futureData):
    futureData, pastData = getWeather()
    x, y, y1, y2 = preparingCurrentData(dict(futureData))
    xFormatted = [dt.datetime.strptime(d[:10]+d[11:], '%Y-%m-%d%H:%M') for d in x ]
    
    
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('exp', color=color)
    ax1.plot(xFormatted, y, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
    ax2.plot(xFormatted, y1, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca()..xaxis.set_major_locator(mdates.DayLocator())
    plt.gca()..xaxis.set_minor_locator(mdates.HourLocator())

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    #plt.show()
    
    
    
    
    '''    fig = Figure(figsize=(5, 3))

    plotCurrentTemp = fig.add_subplot(111)
    plotCurrentTemp.plot(xFormatted, y2)
    plotCurrentTemp.fill(xFormatted,y2)
    plotCurrentTemp.plot(xFormatted, y)
    plotCurrentTemp.plot(xFormatted, y1)'''

    '''    plotCurrentTemp.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plotCurrentTemp.xaxis.set_major_locator(mdates.DayLocator())
    plotCurrentTemp.xaxis.set_minor_locator(mdates.HourLocator())
    plotCurrentTemp.margins(x=0,y=0.05)
    plotCurrentTemp.tick_params(axis='x', labelrotation=30, labelsize=7)'''
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=1, columnspan=2)
    '''    plotCurrentTemp.tick_params(axis='y', labelsize=7)
    plotCurrentTemp.set_ylabel('Degrees (Celsius scale)')
    plotCurrentTemp.set_title('Weather for the next week')
    fig.tight_layout()'''
