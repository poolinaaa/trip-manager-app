from os import name
from PIL import ImageTk
import tkinter as tk
import tkinter.font
from funcBehaviorFrames import appearance
import config as c
from sqlite3 import *
appearance()


class Landmark:
    landmarkId = 1

    def __init__(self, name, address,link) :
        self.name = name
        self.address = address
        self.link = link
        self.id = Landmark.landmarkId
        Landmark.landmarkId += 1

    def checkboxButton(self, frame):
        self.var = tk.IntVar()
        self.button = tk.Checkbutton(master=frame, text=f'{self.name}',variable=self.var, onvalue=1, offvalue=0, justify='left')
        self.button.pack()

    def insertIntoDatabase(self, table, database):
        try:
            con = connect(f'{database}')
            cur = con.cur()
            print("Connected to SQLite")

            sqlite_insert_with_param = f"""INSERT INTO {table}
                            (attractionId,nameOfAttraction,address, wantToSee) 
                            VALUES (?, ?, ?, ?);"""
            if self.var == 1:
                data_tuple = (self.id, self.name, self.address, 'yes')
            else:
                data_tuple = (self.id, self.name, self.address, 'no')

            cur.execute(sqlite_insert_with_param, data_tuple)
            con.commit()
            print("success")

            cur.close()

        except Error as error:
            print("fail", error)
        finally:
            if con:
                con.close()
                print("connection is closed")





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
