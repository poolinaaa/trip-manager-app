from os import name
from PIL import ImageTk
import tkinter as tk
import tkinter.font
from funcBehaviorFrames import appearance
import config as c
from sqlite3 import *
appearance()


class Landmark:

    def __init__(self, name, address,link) :
        self.name = name
        self.address = address
        self.link = link

    def checkboxButton(self, frame):
        self.var = tk.IntVar()
        self.button = tk.Checkbutton(master=frame, text=f'{self.name}',variable=self.var, onvalue=1, offvalue=0, justify='left')
        self.button.pack()

    def insertVaribleIntoTable(self, table, database):
        try:
            sqliteConnection = connect(f'{database}')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = f"""INSERT INTO {table}
                            (id, name, address) 
                            VALUES (?, ?, ?);"""

            data_tuple = (id, self.name, self.address)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("Python Variables inserted successfully into table")

            cursor.close()

        except Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")





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
