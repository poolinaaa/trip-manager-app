import tkinter as tk


class FrameBase(tk.Frame):
    '''class for a base frame'''

    # constructor method for initializing the frame
    def __init__(self, masterWindow, colorOfBg, colorDetails, colorHighlight, countryName,
                 baseCurrency, codeCurrency='', currentRate='unavailable data', **kwargs):
        super().__init__(master=masterWindow, bg=colorOfBg,
                         highlightbackground=colorOfBg, highlightcolor=colorOfBg, **kwargs)
        # shared variables
        self.countryName = countryName
        self.baseCurrency = baseCurrency
        self.codeCurrency = codeCurrency
        self.currentRate = currentRate
        # define fonts
        self.titleFont = {'family': "Lato", 'size': 13, 'weight': "bold"}
        self.questionFont = {'family': "Lato", 'size': 11, 'weight': "bold"}
        self.errorFont = {'family': "Lato", 'size': 9, 'weight': "bold"}
        # colors
        self.colorOfBg = colorOfBg
        self.colorDetails = colorDetails
        self.colorHighlight = colorHighlight

    # loading another frame
    def loadFrame(self, frameToLoad):

        if frameToLoad is not None:
            self.grid_remove()
            frameToLoad.grid()

    # static method for executing multiple functions (to be used in buttons)
    @staticmethod
    def multipleFuncButton(*functions):
        def executingFunctions(*args, **kwargs):
            for func in functions:
                func(*args, **kwargs)
            return executingFunctions

    # clearing entry widgets
    @staticmethod
    def clearEntry(*entries):
        for entry in entries:
            entry.delete(0, tk.END)

    # clearing the view within a frame
    @staticmethod
    def clearView(frame):
        for widget in frame.winfo_children():
            widget.destroy()
