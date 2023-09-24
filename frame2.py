import tkinter as tk
import tkinter.font
import customtkinter
from PIL import ImageTk
import PIL.Image
from datetime import datetime, timedelta
import requests
import json

from funcPlots import PlotsCurrency
from base import FrameBase

class Frame2(FrameBase):
    '''class of currency frame'''
    
    def __init__(self, masterWindow, colorOfBg, colorDetails, colorHighlight, frame1, countryName, baseCurrency, codeCurrency):
        super().__init__(masterWindow=masterWindow,
                         colorOfBg=colorOfBg, colorDetails=colorDetails, colorHighlight=colorHighlight, countryName=countryName, baseCurrency=baseCurrency, codeCurrency=codeCurrency)
        self.dateStart = tk.StringVar()
        self.dateEnd = tk.StringVar()
        self.frame1 = frame1
        self.colorOfBg = colorOfBg
        self.load()
    
    # loading the frame
    def load(self):
        self.tkraise()

        #title and back button
        self.backButton = customtkinter.CTkButton(master=self, text='BACK', fg_color=self.colorDetails, width=40, height=40,
                                                  command=lambda: self.multipleFuncButton(self.clearEntry(self.entryStart, self.entryEnd), self.loadFrame(self.frame1)))
        self.labelTitle = tk.Label(master=self, text="Analyse currency rate",
                                   font=tkinter.font.Font(**self.titleFont), bg=self.colorHighlight, fg='white')
        #frame with entries
        self.frameEnteringDate = tk.Frame(
            master=self, bg=self.colorHighlight, highlightbackground=self.colorOfBg, highlightcolor=self.colorOfBg)

        #create labels, entries and button for entering dates
        #labels
        self.labelStartDate = tk.Label(master=self.frameEnteringDate,
                                       text='Enter the start date: ', fg='white', bg=self.colorHighlight)
        self.labelEndDate = tk.Label(master=self.frameEnteringDate,
                                     text='Enter the end date: ', fg='white', bg=self.colorHighlight)

        #button
        self.buttonConfirmDate = customtkinter.CTkButton(master=self.frameEnteringDate, width=20, text='CONFIRM TIME SPAN', fg_color=self.colorDetails,
                                                         command=self.confirmButton)
        #entries
        self.entryStart = tk.Entry(master=self.frameEnteringDate,
                                   width=28, textvariable=self.dateStart)
        self.entryStart.insert(0, 'YYYY-MM-DD')

        self.entryEnd = tk.Entry(master=self.frameEnteringDate,
                                 width=28, textvariable=self.dateEnd)
        self.entryEnd.insert(0, 'YYYY-MM-DD')
        
        #frame for displaying plots
        self.framePlots = tk.Frame(master=self, bg=self.colorOfBg,
                                   highlightbackground=self.colorOfBg, highlightcolor=self.colorOfBg)
        
        #fake buttons - they will be replaced with real ones after entering dates (there is a problem with changing state of customtkinker buttons)
        self.fake1 = customtkinter.CTkButton(
            master=self.framePlots, width=20, state=tk.DISABLED, text='SHOW PLOT 1', fg_color=self.colorDetails)
        self.fake2 = customtkinter.CTkButton(
            master=self.framePlots, width=20, state=tk.DISABLED, text='SHOW PLOT 2', fg_color=self.colorDetails)
        self.fake3 = customtkinter.CTkButton(
            master=self.framePlots, width=20, state=tk.DISABLED, text='SHOW PLOT 3', fg_color=self.colorDetails)

        #image of some cash
        img = (PIL.Image.open("money.png"))
        resized_image = img.resize((400, 400))
        new_image = ImageTk.PhotoImage(resized_image)
        self.pictureWidget = tk.Label(
            master=self.framePlots, image=new_image, width=400, height=400, bg=self.colorOfBg)
        self.pictureWidget.image = new_image

        #description of plots and their buttons (to choose which plot should be displayed)
        #plot 1 : plot from the given period of time compared to the current rate
        self.labelPlot1 = tk.Label(
            master=self.framePlots, text='Comparison to the current rate', bg=self.colorOfBg, fg='white')
        self.buttonPlot1 = customtkinter.CTkButton(master=self.framePlots, width=20, text='SHOW PLOT 1', fg_color=self.colorDetails,
                                                   command=lambda: PlotsCurrency.createPlotButton(self.dates, self.rate, self.frame1.currentRate, self.framePlots))
        
        #plot 2 : plot from the given period of time compared to the EUR, USD, PLN and CNY
        self.labelPlot2 = tk.Label(
            master=self.framePlots, text='Rate compared to changes \nin EUR, USD, PLN, CNY', bg=self.colorOfBg, fg='white')
        self.buttonPlot2 = customtkinter.CTkButton(master=self.framePlots, width=20, text='SHOW PLOT 2', fg_color=self.colorDetails, command=lambda: PlotsCurrency.createPlotButtonAll(
            self.dates, self.framePlots, self.rate, self.eur, self.usd, self.pln, self.cny, self.code))

        #plot 3 : plot with the rate from the last 30 days
        self.labelPlot3 = tk.Label(
            master=self.framePlots, text='Currency rate for the last 30 days', bg=self.colorOfBg,  fg='white')
        self.buttonPlot3 = customtkinter.CTkButton(master=self.framePlots, width=20, text='SHOW PLOT 3', fg_color=self.colorDetails,
                                                   command=lambda: PlotsCurrency.createPlotButtonLastMonth(self.base, self.code, self.framePlots))

        #packing
        self.backButton.grid(column=0, row=0)
        self.labelTitle.grid(column=1, row=1, padx=60, sticky='ew')
        self.frameEnteringDate.grid(
            column=1, row=2, pady=20, padx=60, sticky='ew')

        self.labelStartDate.grid(column=0, row=0)
        self.labelEndDate.grid(column=1, row=0)

        self.buttonConfirmDate.grid(column=3, row=1, padx=10, pady=5)

        self.entryStart.grid(column=0, row=1, padx=5, pady=5)
        self.entryEnd.grid(column=1, row=1, padx=5, pady=5)
        
        for nr, btn in enumerate([self.fake1, self.fake2, self.fake3], start = 0):
            btn.grid(column=nr, row=1, padx=15, pady=10)
            
        self.pictureWidget.grid(
            column=0, row=2, columnspan=3, pady=10, sticky='ew')

        for nr, label in enumerate([self.labelPlot1, self.labelPlot2, self.labelPlot3], start = 0):
            label.grid(column=nr, row=0, padx=15)

        self.framePlots.grid(column=1, row=4, padx=60, sticky='ew')

    #button - confirm entered dates
    def confirmButton(self):
        #get code of base currency and currency of the destination country
        self.base = self.frame1.baseCurrName
        self.code = self.frame1.codeCurrency
        
        #cut-off dates
        start = self.dateStart.get()
        end = self.dateEnd.get()
        
        #get rates of currencies in chosen range of dates
        if (self.checkDate(start) and self.checkDate(end)):

            headers = {"apikey": "uk5pSwPkDIdeHqRIJbOTBWjr9YT3T73E"}
            params = {'start_date': start, 'end_date': end,
                      'base': self.base, 'symbols': f'{self.code},EUR,USD,PLN,CNY'}
            r = requests.get(
                'https://api.apilayer.com/fixer/timeseries', params=params, headers=headers)
            print(r)
            try:
                self.currencyData = r.json()
            except json.JSONDecodeError:
                print('Wrong format of currencyData.')
            else:
                #prepare data for the plots
                self.preparingData(self.code)
                
                #replacing fake buttons with real ones
                for btn in (self.fake1,self.fake2,self.fake3):
                    btn.destroy()
                for nr, btn in enumerate([self.buttonPlot1,self.buttonPlot2, self.buttonPlot3],start=0):
                    btn.grid(column=nr, row=1, padx=15, pady=10)
                

        else:
            #warning : incorrect date
            incorrectDate = tk.Label(
                master=self, text='wrong format of date, try again', font=tkinter.font.Font(**self.errorFont), bg=self.colorHighlight, fg='white')
            incorrectDate.grid(column=1, row=3, padx=60, sticky='ew')
            self.after(5000, incorrectDate.destroy)

    #checking format of entered date
    def checkDate(self, date):
        try:
            isDateCorrect = datetime.strptime(date, '%Y-%m-%d')
            return True
        except:
            return False

    #preparing data for plots
    def preparingData(self, code):
        self.dates = []
        self.rate = []
        self.eur = []
        self.usd = []
        self.pln = []
        self.cny = []

        #get start and end date in range
        start_date = self.currencyData["start_date"]
        end_date = self.currencyData["end_date"]

        #go through every date and append every currency rate (from everyday in chosen range)
        current_date = start_date
        while current_date <= end_date:
            rates_for_date = self.currencyData["rates"][current_date]
            self.eur.append(rates_for_date["EUR"])
            self.usd.append(rates_for_date["USD"])
            self.pln.append(rates_for_date["PLN"])
            self.cny.append(rates_for_date["CNY"])
            self.rate.append(rates_for_date[code])
            self.dates.append(current_date)
            current_date = (datetime.strptime(
                current_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
