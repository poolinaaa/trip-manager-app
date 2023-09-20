import tkinter as tk
from tkinter import *

class FrameBase(tk.Frame):

    def __init__(self, masterWindow, colorOfBg, colorDetails, colorHighlight, countryName, baseCurrency, **kwargs):
        super().__init__(master=masterWindow, bg=colorOfBg,
                         highlightbackground=colorOfBg, highlightcolor=colorOfBg, **kwargs)
        self.countryName = countryName
        self.baseCurrency = baseCurrency
        self.titleFont = {'family':"Lato", 'size':13, 'weight':"bold"}
        self.questionFont = {'family':"Lato", 'size':11, 'weight':"bold"}
        self.errorFont = {'family':"Lato", 'size':9, 'weight':"bold"}
        self.colorOfBg = colorOfBg
        self.colorDetails = colorDetails
        self.colorHighlight = colorHighlight


    def loadFrame(self, frameToLoad):
        
        if frameToLoad is not None:
            self.grid_remove() 
            frameToLoad.grid()
    
    @staticmethod      
    def multipleFuncButton(*functions):
        def executingFunctions(*args, **kwargs):
            for func in functions:
                func(*args, **kwargs)
            return executingFunctions

    @staticmethod
    def clearEntry(*entries):
        for entry in entries:
            entry.delete(0, tk.END)

    @staticmethod
    def clearView(frame):
        for widget in frame.winfo_children():
            widget.destroy()