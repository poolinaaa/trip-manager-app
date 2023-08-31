from PIL import ImageTk
import tkinter as tk
import tkinter.font
from funcBehaviorFrames import appearance
import config as c
from sqlite3 import *
import webbrowser
appearance()


class ThemeSection(tk.Frame):

    def __init__(self, masterFrame, **kwargs):
        super().__init__(master=masterFrame, width=100, padx=10, bg='red',
                         highlightbackground=c.bgColor, highlightcolor=c.bgColor, **kwargs)
        self.headingF = tkinter.font.Font(family="Lato", size=11)
        self.textF = tkinter.font.Font(family="Lato", size=8)

    def addTitleLabel(self, title: str):
        self.title = tk.Label(
            self, text=title, width=30,font=self.headingF, bg='green', fg='white')
        self.title.pack(pady=10)

    def addImage(self, nameOfFile):
        self.pictureSection = ImageTk.PhotoImage(file=nameOfFile)
        self.pictureWidget = tk.Label(
            master=self, image=self.pictureSection, bg=c.bgColor, width=100, height=100)
        self.pictureWidget.image = self.pictureSection
        self.pictureWidget.pack(pady=10)


class InitializationFrame(tk.Frame):

    def __init__(self, masterWindow, **kwargs):
        super().__init__(master=masterWindow, width=300, height=500, bg=c.bgColor,
                         highlightbackground=c.bgColor, highlightcolor=c.bgColor, **kwargs)
