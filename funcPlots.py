import requests
import json
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import date, timedelta
import datetime as dt
import matplotlib.dates as mdates


class PlotsCurrency():
    '''class for creating currency-related plots'''

    # create a plot comparing a specific period's rate with the current rate
    @staticmethod
    def createPlotButton(dates, rates, current, parent):

        # prepare data
        y = rates
        currRate = [current for _ in range(len(dates))]

        xFormatted = [dt.datetime.strptime(d, '%Y-%m-%d') for d in dates]

        fig, ax1 = plt.subplots(figsize=(6, 3.2))

        # set plot properties
        color = 'maroon'
        ax1.set_ylabel('Rate', fontsize=8)
        ax1.plot(xFormatted, y, color=color,
                 label=f'Rate from {dates[0][0:10]} to {dates[-1][0:10]}')
        color = 'teal'
        ax1.plot(xFormatted, currRate, color=color, label='Current rate')

        ax1.tick_params(axis='y', labelsize=8)
        ax1.margins(x=0, y=0.05)
        ax1.tick_params(axis='x', labelrotation=30, labelsize=6)
        ax1.set_title(
            'Comparison between the rate from a specific period and the current rate', fontsize=10)

        ax1.legend(loc='upper left', fontsize=7)

        # date labels format
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

        # placing the graph
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=2, columnspan=3, pady=10)

    # create a plot comparing a currency with EUR, USD, PLN, and CNY
    @staticmethod
    def createPlotButtonAll(dates, parent, ratesChosenCountry, EUR, USD, PLN, CNY, codeCurrency):

        # prepare data
        y = ratesChosenCountry
        xFormatted = [dt.datetime.strptime(d, '%Y-%m-%d') for d in dates]

        e = EUR
        u = USD
        p = PLN
        c = CNY

        fig, ax1 = plt.subplots(figsize=(6, 3.2))

        # set plot properties
        color = 'rebeccapurple'
        ax1.set_ylabel('Rate', fontsize=8)
        ax1.plot(xFormatted, y, color=color,
                 label=codeCurrency)
        color = 'teal'
        if codeCurrency != 'EUR':
            ax1.plot(xFormatted, e, color=color, label='EUR')
        color = 'dodgerblue'
        if codeCurrency != 'USD':
            ax1.plot(xFormatted, u, color=color, label='USD')
        color = 'maroon'
        if codeCurrency != 'PLN':
            ax1.plot(xFormatted, p, color=color, label='PLN')
        color = 'turquoise'
        if codeCurrency != 'CNY':
            ax1.plot(xFormatted, c, color=color, label='CNY')

        ax1.tick_params(axis='y', labelsize=8)
        ax1.margins(x=0, y=0.05)
        ax1.tick_params(axis='x', labelrotation=30, labelsize=6)
        ax1.set_title(
            'Comparison between EUR, USD, PLN, CNY and currency in chosen country', fontsize=10)

        ax1.legend(loc='upper left', fontsize=7)

        # date labels format
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

        # placing the graph
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=2, columnspan=3, pady=10)

    # create a plot for the last 30 days' rate changes
    @staticmethod
    def createPlotButtonLastMonth(baseCurrName, codeCurrency, parent):

        # calculate date range for the last 30 days
        today = date.today()
        monthAgo = today - timedelta(days=30)

        # API request headers and parameters
        headers = {
            "apikey": "YOUR API KEY"
        }
        params = {'start_date': monthAgo, 'end_date': today,
                  'base': baseCurrName, 'symbols': f'{codeCurrency},EUR,USD,PLN,CNY'}
        r = requests.get(
            'https://api.apilayer.com/fixer/timeseries', params=params, headers=headers)

        # check the response
        try:
            currencyData = r.json()
        except json.JSONDecodeError:
            print('Wrong format of data.')
        else:
            # date and rate data from the response
            dates = [date for date in currencyData['rates']]
            xFormatted = [dt.datetime.strptime(d, '%Y-%m-%d') for d in dates]
            rate = [currencyData['rates'][date][codeCurrency]
                    for date in currencyData['rates']]
            y = rate

            fig, ax1 = plt.subplots(figsize=(6, 3.2))

            # set plot properties
            color = 'teal'
            ax1.set_ylabel('Rate', fontsize=8)
            ax1.plot(xFormatted, y, color=color,
                     label=f'Rate from {dates[0][0:10]} to {dates[-1][0:10]}')

            ax1.tick_params(axis='y', labelsize=8)
            ax1.margins(x=0, y=0.05)
            ax1.tick_params(axis='x', labelrotation=30, labelsize=6)
            ax1.set_title(
                'Changes in rate for the last 30 days', fontsize=10)

            ax1.legend(loc='upper left', fontsize=7)

            # date labels format
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

            # placing the graph
            fig.tight_layout()
            canvas = FigureCanvasTkAgg(fig, master=parent)
            canvas.draw()
            canvas.get_tk_widget().grid(column=0, row=2, columnspan=3, pady=10)
