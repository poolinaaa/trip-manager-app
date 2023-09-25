import tkinter as tk
from tkcalendar import *
import customtkinter
import tkinter.font
from PIL import ImageTk
import PIL.Image
import webbrowser
from sqlite3 import *
import csv

from geoFunc import GeographyData
from base import FrameBase


class Frame3(FrameBase):
    '''class of geography frame'''

    def __init__(self, masterWindow, colorOfBg, colorDetails, colorHighlight, frame1, countryName, baseCurrency):
        super().__init__(masterWindow=masterWindow,
                         colorOfBg=colorOfBg, colorDetails=colorDetails, colorHighlight=colorHighlight, countryName=countryName, baseCurrency=baseCurrency)

        self.frame1 = frame1
        self.colorOfBg = colorOfBg
        self.load()

    # loading the frame
    def load(self):
        self.tkraise()

        # title and back button
        self.labelTitle = tk.Label(master=self, text=f"Discover some geographical facts",
                                   font=tkinter.font.Font(**self.titleFont), bg=self.colorOfBg, fg='white')
        self.backButton = customtkinter.CTkButton(master=self, text='BACK', fg_color=self.colorDetails, width=40, height=40,
                                                  command=lambda: self.loadFrame(self.frame1))

        # options to choose section
        # departure country
        self.frameOptions = tk.Frame(self, bg=self.colorHighlight)

        self.labelDepartureCountry = tk.Label(master=self.frameOptions, text="What is your departure country?",
                                              width=30, font=tkinter.font.Font(**self.questionFont), bg=self.colorOfBg, fg='white', anchor="w")

        self.departureCountry = tk.StringVar(value='country')
        self.entryDepartureCountry = tk.Entry(
            master=self.frameOptions, textvariable=self.departureCountry)

        # unit of distance
        self.labelUnit = tk.Label(master=self.frameOptions, text='Select the unit in which the distance will be displayed',
                                  font=tkinter.font.Font(**self.questionFont), bg=self.colorOfBg, fg='white', anchor="w")
        var = tk.StringVar(value='kilometers')

        self.kmButton = tk.Radiobutton(
            master=self.frameOptions, text='kilometers', variable=var, value='kilometers', bg='#9dc0d1')
        self.milesButton = tk.Radiobutton(
            master=self.frameOptions, text='miles', variable=var, value='miles', bg='#9dc0d1')

        # confirm choices
        self.buttonConfirmCountry = customtkinter.CTkButton(master=self.frameOptions, text='CONFIRM COUNTRY', fg_color=self.colorDetails,
                                                            command=lambda: self.confirmCountry(var.get()))

        # frames with facts
        self.frameCities = tk.Frame(self, bg=self.colorHighlight, height=450)
        self.frameCheckbutton = tk.Frame(
            master=self, bg='#9dc0d1', width=300, height=450)

        # globe picture
        img = (PIL.Image.open("globe.png"))
        resized_image = img.resize((300, 300))
        new_image = ImageTk.PhotoImage(resized_image)
        self.pictureWidget = tk.Label(
            master=self.frameCheckbutton, image=new_image, width=300, height=300, bg=self.colorOfBg)
        self.pictureWidget.image = new_image

        # packing widgets
        # options, title, back button
        self.backButton.grid(column=0, row=0)
        self.labelTitle.grid(column=1, row=1, columnspan=2)
        self.frameOptions.grid(column=1, row=2, columnspan=2)
        self.buttonConfirmCountry.grid(row=2, column=0, columnspan=3, pady=20)

        # everything inside options section
        self.labelDepartureCountry.grid(column=0, row=0)
        self.entryDepartureCountry.grid(column=0, row=1)
        self.labelUnit.grid(column=1, row=0, columnspan=2)
        self.kmButton.grid(column=1, row=1, pady=5)
        self.milesButton.grid(column=2, row=1, pady=5)

        # frames with facts
        self.frameCities.grid(column=1, row=3, pady=20, sticky='n')
        self.pictureWidget.pack()
        self.frameCheckbutton.grid(column=2, row=3, pady=20, sticky='n')

    # button - confirm departure country and unit of distance
    def confirmCountry(self, unit):

        # replace image with information about landmarks
        for widget in self.frameCheckbutton.winfo_children():
            widget.destroy()

        baseCountry = self.departureCountry.get().capitalize()
        baseCountry = self.checkingCountry(baseCountry)

        # searching landmarks near the capital of destination
        # check longitude and latitude
        with open('worldcities.csv', encoding='utf8') as csvFile:
            csvRead = csv.reader(csvFile, delimiter=',')
            latBase = None
            lngBase = None
            for row in csvRead:
                if row[4] == baseCountry:
                    latBase = row[2]
                    lngBase = row[3]
                    break

            destinationGeoInfo: dict = GeographyData(
            ).searchInfoAboutDestination(self.countryName)

            # distance between capitals of departure and destination country
            distance = GeographyData().getDistanceBetweenPoints(
                latBase, lngBase, destinationGeoInfo['lat'], destinationGeoInfo['lng'], unit)

            distanceLabel = tk.Label(
                master=self.frameCheckbutton,
                text=f'Distance between {baseCountry} and {self.countryName.get().capitalize()} is about \n{distance} {unit}',
                font=tkinter.font.Font(**self.questionFont), bg=self.colorHighlight, fg='white', anchor="w")

            # checking attractions nearby
            attractions = GeographyData().searchAttractions(
                destinationGeoInfo['lng'], destinationGeoInfo['lat'])

            listOfAttractions = list()

            for attr in attractions['features']:
                ds = attr['properties']['datasource']
                raw = ds.get('raw', {})
                image_url = raw.get('image', '')
                landmark = AttractionToSee(attr['properties']['address_line1'],
                                           attr['properties']['address_line2'],
                                           image_url)
                listOfAttractions.append(landmark)
                landmark.checkboxButton(self.frameCheckbutton)

            # saving chosen attractions in the db and opening pages in the webbrowser
            buttonSave = customtkinter.CTkButton(master=self.frameCheckbutton, text='SAVE AND OPEN IN THE BROWSER', fg_color=self.colorDetails,
                                                 command=lambda: GeographyData().savingLandmarks(listOfAttractions))
            # packing
            distanceLabel.pack()
            buttonSave.pack(pady=10)

    # checking if entered country is correct
    def checkingCountry(self, country):
        with open('countries.csv', encoding='utf8') as csvFile:
            csvRead = csv.reader(csvFile, delimiter=',')
            for row in csvRead:
                if row[2] == country:
                    foundCountry = row[2]

            if 'foundCountry' not in locals():
                return 'CountryError'
            else:
                return foundCountry


class AttractionToSee:
    '''class of landmarks found nearby capital of destination country'''

    AttractionToSeeId = 1

    def __init__(self, name, address, link=None):
        self.name = name
        self.address = address
        self.link = link
        self.errorFont = {'family': "Lato", 'size': 9, 'weight': "bold"}
        self.id = AttractionToSee.AttractionToSeeId
        AttractionToSee.AttractionToSeeId += 1

    # creating checkbox with attraction
    def checkboxButton(self, frame):
        self.var = tk.IntVar()
        self.button = tk.Checkbutton(
            master=frame, text=f'{self.name}', variable=self.var, onvalue=1, offvalue=0,
            justify='left', bg='#9dc0d1', font=tkinter.font.Font(**self.errorFont))
        self.button.pack(anchor='w')

    # inserting attraction in the db
    def insertIntoDatabase(self, table, database):
        try:
            con = connect(f'{database}.db')
            cur = con.cursor()
            print("connected")

            insertAttraction = f"""INSERT INTO {table}
                            (nameOfAttraction,address, wantToSee) 
                            VALUES (?, ?, ?);"""
            if self.var.get() == 1:
                data = (self.name, self.address, 'yes')
            else:
                data = (self.name, self.address, 'no')

            cur.execute(insertAttraction, data)
            con.commit()
            cur.close()

        except Error as error:
            print("fail", error)

        finally:
            if con:
                con.close()
                print("connection is closed")

    # searching chosen attraction in the webbrowser
    def openInTheBrowser(self):
        if self.name != None:
            url = "https://www.google.com.tr/search?q={}".format(self.name)
            webbrowser.open_new_tab(url)
        else:
            print('There is not any link')
