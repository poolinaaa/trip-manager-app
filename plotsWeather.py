from weather import getWeather
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def preparingPastData(pastData: dict):
    days = pastData['daily']['time']
    temperature = pastData['daily']['temperature_2m_mean']
    return days, temperature


def createPlotWeatherYearAgo(parent, pastData):
    futureData, pastData = getWeather()
    x, y = preparingPastData(dict(pastData))
    fig = Figure(figsize=(4, 2), dpi=100)
    plotPast = fig.add_subplot(111)

    plotPast.plot(list(range(0, len(x))), y,)
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0,row=1, columnspan=2)

def preparingCurrentData(futureData: dict):
    time = futureData['hourly']['time']
    temperature = futureData['hourly']['temperature_2m']
    precipitationProb=futureData['hourly']['precipitation_probability']
    precipitation=futureData['hourly']['precipitation']
    
    return time, temperature, precipitationProb, precipitation


def createPlotWeatherCurrent(parent, futureData):
    futureData, pastData = getWeather()
    x, y, y1, y2 = preparingCurrentData(dict(futureData))
    xRange = list(range(0, len(x)))
    fig = Figure(figsize=(4, 2), dpi=100)
    
    plotCurrentTemp = fig.add_subplot(111)
    plotCurrentTemp.plot(xRange, y, xRange, y1, xRange, y2)

    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0,row=1, columnspan=2)