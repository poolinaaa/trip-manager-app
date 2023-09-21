import tkinter as tk
from ctypes import windll

from frame1 import Frame1
from frame2 import Frame2
from frame3 import Frame3
from frame4 import Frame4


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('WanderWisely')
        self.geometry("918x700")
        self.minsize(918, 700)
        self.maxsize(918, 700)
        self.bgColor = '#295873'
        self.highlight = '#1c3c4f'
        self.details = '#162f3d'
        self.configure(background=self.bgColor)
        self.countryName = tk.StringVar(value='your country')
        self.baseCurrency = tk.StringVar(value='your base currency')
        self.codeCurrency = tk.StringVar(value='codeCurrency')
        self.start()
        

    def start(self):
        self.frame1 = Frame1(self, self.bgColor, self.details, self.highlight, self.countryName, self.baseCurrency, self.codeCurrency)
        self.frame2 = Frame2(self, self.bgColor, self.details, self.highlight, self.frame1, self.countryName, self.baseCurrency, self.codeCurrency)
        self.frame3 = Frame3(self, self.bgColor, self.details, self.highlight, self.frame1, self.countryName, self.baseCurrency)
        self.frame4 = Frame4(self, self.bgColor, self.details, self.highlight, self.frame1, self.countryName, self.baseCurrency)

        self.frame1.setFrames(self.frame1, self.frame2,
                              self.frame3, self.frame4)

        for frame in (self.frame1, self.frame2, self.frame3, self.frame4):

            frame.grid(row=0, column=0, sticky='nsew')

        self.frame1.grid(row=0, column=0, sticky='nsew')
        self.frame2.grid_remove()
        self.frame3.grid_remove()
        self.frame4.grid_remove()

    def clearView(self):
        self.frame1.grid_remove()
        self.frame2.grid_remove()
        self.frame3.grid_remove()
        self.frame4.grid_remove()



windll.shcore.SetProcessDpiAwareness(1)

app = Window()

app.mainloop()
