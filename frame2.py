import tkinter as tk
from funcBehaviorFrames import confirmButton
import config as c
from funcPlots import createPlotButton, createPlotButtonAll, createPlotButtonLastMonth
import customtkinter
from tkinter import *
from PIL import ImageTk
import config as c
from tkinter import *
from sqlite3 import *
import PIL.Image
from base import FrameBase
import tkinter.font

class Frame2(FrameBase):

    def __init__(self, masterWindow, colorOfBg, colorDetails, colorHighlight, frame1, countryName, baseCurrency):
        super().__init__(masterWindow=masterWindow,
                         colorOfBg=colorOfBg, colorDetails=colorDetails, colorHighlight=colorHighlight, countryName=countryName, baseCurrency=baseCurrency)
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
                                                         command=lambda: confirmButton(self, self.dateStart, self.dateEnd, baseCurrName, codeCurrency, self.fake1, self.fake2, self.fake3, self.buttonPlot1, self.buttonPlot2, self.buttonPlot3))
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
                                                   command=lambda: createPlotButton(c.dates, c.rate, c.current, self.framePlots))

        self.labelPlot2 = tk.Label(
            master=self.framePlots, text='Rate compared to changes \nin EUR, USD, PLN, GBP', bg=self.colorOfBg, fg='white')
        self.labelPlot2.grid(column=1, row=0, padx=15)

        self.buttonPlot2 = customtkinter.CTkButton(master=self.framePlots, width=20, text='SHOW PLOT 2', fg_color=self.colorDetails, command=lambda: createPlotButtonAll(
            c.dates, self.framePlots, c.rate, c.eur, c.usd, c.pln, c.cny, codeCurrency))

        self.labelPlot3 = tk.Label(
            master=self.framePlots, text='Currency rate for the last 30 days', bg=self.colorOfBg,  fg='white')
        self.labelPlot3.grid(column=2, row=0, padx=15)

        self.buttonPlot3 = customtkinter.CTkButton(master=self.framePlots, width=20, text='SHOW PLOT 3', fg_color=self.colorDetails,
                                                   command=lambda: createPlotButtonLastMonth(baseCurrName, codeCurrency, self.framePlots))

        self.framePlots.pack()
