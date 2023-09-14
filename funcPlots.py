import requests
import json
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import date, timedelta
import datetime as dt
import matplotlib.dates as mdates



def createPlotButton(dates, rates, current, parent):
    y = rates
    x = {num: date for num, date in enumerate(dates)}
    currRate = [current for _ in range(len(dates))]
    
    xFormatted = [dt.datetime.strptime(d, '%Y-%m-%d') for d in dates ]

    fig, ax1 = plt.subplots(figsize=(6, 3.2))
    
    color = 'maroon'
    ax1.set_ylabel('rate', color=color, fontsize= 7)
    ax1.plot(xFormatted, y, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.tick_params(axis='y', labelsize=5)
    ax1.margins(x=0,y=0.05)
    ax1.tick_params(axis='x', labelrotation=30, labelsize=6)
    ax1.set_title('Ratees',fontsize=11)
    
    
    ax2 = ax1.twinx()
    color = 'teal'
    ax2.set_ylabel('Precipitation [mm]', color=color, fontsize= 7) 
    ax2.plot(xFormatted, currRate, color=color)
    
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.tick_params(axis='y', labelsize=6)
    ax2.margins(x=0,y=0.05)
    
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    

    fig.tight_layout()
 
    
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=2, columnspan=3, pady=10)


def createPlotButtonAll(dates, parent, ratesChosenCountry, EUR, USD, PLN, GBP):
    y = ratesChosenCountry
    x = {num: date for num, date in enumerate(dates)}
    ox = list(range(0, len(dates)))
    e = EUR
    u = USD
    p = PLN
    g = GBP

    fig = Figure(figsize=(5, 3))

    plot1 = fig.add_subplot(111)

    plot1.plot(ox, y, ox, e, ox, u, ox, p, ox, g)

    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=2, columnspan=3, pady=10)
    plot1.set_xlabel('X Label')
    plot1.set_ylabel('Y Label')
    plot1.set_title('Plot Title')
    fig.tight_layout()


def createPlotButtonLastMonth(baseCurrName, codeCurrency, parent):

    today = date.today()
    monthAgo = today - timedelta(days=30)

    params = {'start_date': monthAgo, 'end_date': today,
              'base': baseCurrName, 'symbols': codeCurrency}
    r = requests.get('https://api.exchangerate.host/timeseries/', params)
    print(r)
    try:
        currencyData = r.json()
    except json.JSONDecodeError:
        print('Wrong format of data.')
    else:
        print(currencyData)
        dates = [date for date in currencyData['rates']]
        rate = [currencyData['rates'][date][codeCurrency]
                for date in currencyData['rates']]
        y = rate
        x = {num: date for num, date in enumerate(dates)}

        fig = Figure(figsize=(5, 3))
        plot1 = fig.add_subplot(111)

        plot1.plot(list(range(0, len(dates))), y)

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=2, columnspan=3, pady=10)
        plot1.set_xlabel('X Label')
        plot1.set_ylabel('Y Label')
        plot1.set_title('Plot Title')
        fig.tight_layout()
