import tkinter as tk
from funcPlots import PlotsCurrency
import customtkinter
from PIL import ImageTk

from tkinter import *
from sqlite3 import *
import PIL.Image
from base import FrameBase
import tkinter.font


import requests
import json
from datetime import datetime

class Frame2(FrameBase):

    def __init__(self, masterWindow, colorOfBg, colorDetails, colorHighlight, frame1, countryName, baseCurrency, codeCurrency):
        super().__init__(masterWindow=masterWindow,
                         colorOfBg=colorOfBg, colorDetails=colorDetails, colorHighlight=colorHighlight, countryName=countryName, baseCurrency=baseCurrency, codeCurrency=codeCurrency)
        self.dateStart = tk.StringVar()
        self.dateEnd = tk.StringVar()
        self.frame1 = frame1
        self.colorOfBg = colorOfBg
        self.load()

    def load(self):
        self.tkraise()

        self.backButton = customtkinter.CTkButton(master=self, text='BACK', fg_color=self.colorDetails, width=40, height=40,
                                                  command=lambda: self.multipleFuncButton(self.clearEntry(self.entryStart, self.entryEnd), self.loadFrame(self.frame1)))
        self.backButton.pack(side=TOP, anchor=NW)

        self.labelTitle = tk.Label(master=self, text="Analyse currency rate",
                                   font=tkinter.font.Font(**self.titleFont), bg=self.colorHighlight, fg='white')
        self.labelTitle.pack()

        self.frameEnteringDate = tk.Frame(
            master=self, bg=self.colorHighlight, highlightbackground=self.colorOfBg, highlightcolor=self.colorOfBg)
        self.frameEnteringDate.pack(pady=20)

        self.labelStartDate = tk.Label(master=self.frameEnteringDate,
                                       text='Enter the start date: ', fg='white', bg=self.colorHighlight)
        self.labelStartDate.grid(column=0, row=0)

        self.labelEndDate = tk.Label(master=self.frameEnteringDate,
                                     text='Enter the end date: ', fg='white', bg=self.colorHighlight)
        self.labelEndDate.grid(column=1, row=0)

        self.buttonConfirmDate = customtkinter.CTkButton(master=self.frameEnteringDate, width=20, text='CONFIRM TIME SPAN', fg_color=self.colorDetails,
                                                         command=self.confirmButton)
        self.buttonConfirmDate.grid(column=3, row=1, padx=10, pady=5)

        self.entryStart = tk.Entry(master=self.frameEnteringDate,
                                   width=28, textvariable=self.dateStart)
        self.entryStart.insert(0, 'YYYY-MM-DD')
        self.entryStart.grid(column=0, row=1, padx=5, pady=5)

        self.entryEnd = tk.Entry(master=self.frameEnteringDate,
                                 width=28, textvariable=self.dateEnd)

        self.entryEnd.insert(0, 'YYYY-MM-DD')
        self.entryEnd.grid(column=1, row=1, padx=5, pady=5)

        self.framePlots = tk.Frame(master=self, bg=self.colorOfBg,
                                   highlightbackground=self.colorOfBg, highlightcolor=self.colorOfBg)

        self.fake1 = customtkinter.CTkButton(
            master=self.framePlots, width=20, state=DISABLED, text='SHOW PLOT 1', fg_color=self.colorDetails)
        self.fake2 = customtkinter.CTkButton(
            master=self.framePlots, width=20, state=DISABLED, text='SHOW PLOT 2', fg_color=self.colorDetails)
        self.fake3 = customtkinter.CTkButton(
            master=self.framePlots, width=20, state=DISABLED, text='SHOW PLOT 3', fg_color=self.colorDetails)
        self.fake1.grid(column=0, row=1, padx=15, pady=10)
        self.fake2.grid(column=1, row=1, padx=15, pady=10)
        self.fake3.grid(column=2, row=1, padx=15, pady=10)

        img = (PIL.Image.open("money.png"))

        resized_image = img.resize((400, 400))
        new_image = ImageTk.PhotoImage(resized_image)

        self.pictureWidget = tk.Label(
            master=self.framePlots, image=new_image, width=400, height=400, bg=self.colorOfBg)

        self.pictureWidget.image = new_image
        self.pictureWidget.grid(column=0, row=2, columnspan=3, pady=10)

        self.labelPlot1 = tk.Label(
            master=self.framePlots, text='Comparison to the current rate', bg=self.colorOfBg, fg='white')
        self.labelPlot1.grid(column=0, row=0, padx=15)

        self.buttonPlot1 = customtkinter.CTkButton(master=self.framePlots, width=20, text='SHOW PLOT 1', fg_color=self.colorDetails,
                                                   command=lambda: PlotsCurrency.createPlotButton(self.dates, self.rate, self.currentRate, self.framePlots))

        self.labelPlot2 = tk.Label(
            master=self.framePlots, text='Rate compared to changes \nin EUR, USD, PLN, GBP', bg=self.colorOfBg, fg='white')
        self.labelPlot2.grid(column=1, row=0, padx=15)

        self.buttonPlot2 = customtkinter.CTkButton(master=self.framePlots, width=20, text='SHOW PLOT 2', fg_color=self.colorDetails, command=lambda: PlotsCurrency.createPlotButtonAll(
            self.dates, self.framePlots, self.rate, self.eur, self.usd, self.pln, self.cny, self.codeCurrency))

        self.labelPlot3 = tk.Label(
            master=self.framePlots, text='Currency rate for the last 30 days', bg=self.colorOfBg,  fg='white')
        self.labelPlot3.grid(column=2, row=0, padx=15)

        self.buttonPlot3 = customtkinter.CTkButton(master=self.framePlots, width=20, text='SHOW PLOT 3', fg_color=self.colorDetails,
                                                   command=lambda: PlotsCurrency.createPlotButtonLastMonth(self.baseCurrency, self.codeCurrency, self.framePlots))

        self.framePlots.pack()

    def confirmButton(self):

        start = self.dateStart.get()
        end = self.dateEnd.get()
        if (self.checkDate(start) and self.checkDate(end)):
            params = {'start_date': start, 'end_date': end,
                    'base': self.baseCurrency, 'symbols': f'{self.codeCurrency},EUR,USD,PLN,CNY'}
            r = requests.get('https://api.exchangerate.host/timeseries/', params)
            print(r)
            try:
                self.currencyData = r.json()
            except json.JSONDecodeError:
                print('Wrong format of c.currencyData.')
            else:
                self.preparingData()
                self.fake1.destroy()
                self.fake2.destroy()
                self.fake3.destroy()
                self.buttonPlot1.grid(column=0, row=1, padx=15, pady=10)
                self.buttonPlot2.grid(column=0, row=1, padx=15, pady=10)
                self.buttonPlot3.grid(column=0, row=1, padx=15, pady=10)

        else:
            incorrectDate = tk.Label(
                master=self, text='wrong format of date, try again', font=tkinter.font.Font(**self.errorFont), bg=self.colorHighlight, fg='white')
            incorrectDate.pack()
            self.after(5000, incorrectDate.destroy)
            
    def checkDate(self, date):
        try:
            isDateCorrect = datetime.strptime(date, '%Y-%m-%d')
            return True
        except:
            return False
        
    def preparingData(self):
        self.dates = [date for date in self.currencyData['rates']]
        self.rate = [self.currencyData['rates'][date][self.codeCurrency] for date in self.currencyData['rates']]
        self.eur = [self.currencyData['rates'][date]['EUR'] for date in self.currencyData['rates']]
        self.usd = [self.currencyData['rates'][date]['USD'] for date in self.currencyData['rates']]
        self.pln = [self.currencyData['rates'][date]['PLN'] for date in self.currencyData['rates']]
        self.cny = [self.currencyData['rates'][date]['CNY'] for date in self.currencyData['rates']]