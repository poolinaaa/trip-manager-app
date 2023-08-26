from PIL import ImageTk
import tkinter as tk
import tkinter.font
from funcBehaviorFrames import appearance
import config as c
appearance()


class Landmark:

    def __init__(self) -> None:
        pass

    def saveLandmark(self):
        pass

    def addToDatabase(self):
        pass


class ThemeSection(tk.Frame):

    def __init__(self, masterFrame, **kwargs):
        super().__init__(master=masterFrame, padx=20, width=200, bg=c.bgColor,
                         highlightbackground=c.bgColor, highlightcolor=c.bgColor, **kwargs)
        self.headingF = tkinter.font.Font(family="Lato", size=11)
        self.textF = tkinter.font.Font(family="Lato", size=8)

    def addTitleLabel(self, title: str):
        self.title = tk.Label(
            self, text=title, font=self.headingF, bg=c.bgColor, fg='white')
        self.title.pack()

    def addImage(self, nameOfFile):
        self.pictureSection = ImageTk.PhotoImage(file=nameOfFile)
        self.pictureWidget = tk.Label(
            master=self, image=self.pictureSection, bg=c.bgColor, width=100, height=100)
        self.pictureWidget.image = self.pictureSection
        self.pictureWidget.pack()


class InitializationFrame(tk.Frame):

    def __init__(self, masterWindow, **kwargs):
        super().__init__(master=masterWindow, width=700, height=600, bg=c.bgColor,
                         highlightbackground=c.bgColor, highlightcolor=c.bgColor, **kwargs)
