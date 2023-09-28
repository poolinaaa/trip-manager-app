import tkinter as tk
from ctypes import windll
import os
from frame1 import Frame1
from frame2 import Frame2
from frame3 import Frame3
from frame4 import Frame4


class Window(tk.Tk):
    '''class of a custom window that inherits from Tkinter's Tk class'''

    def __init__(self):
        super().__init__()

        # setting parameters of the window (title, size, colors)
        self.title('Wander Wisely')
        self.photo = tk.PhotoImage(file= os.path.join(os.path.dirname(__file__), 'images', 'map.png'))
        
        self.iconphoto(False, self.photo)
        self.geometry("918x700")
        self.minsize(918, 700)
        self.maxsize(918, 700)
        self.bgColor = '#295873'
        self.highlight = '#1c3c4f'
        self.details = '#162f3d'
        self.configure(background=self.bgColor)

        # shared variables between frames
        self.countryName = tk.StringVar(value='your country')
        self.baseCurrency = tk.StringVar(value='your base currency')
        self.codeCurrency = tk.StringVar(value='codeCurrency')

        # call the start method to initialize the frames
        self.start()

    def start(self):
        # create instances of custom frame classes and pass necessary parameters

        self.frame1 = Frame1(self, self.bgColor, self.details, self.highlight,
                             self.countryName, self.baseCurrency, self.codeCurrency)
        self.frame2 = Frame2(self, self.bgColor, self.details, self.highlight,
                             self.frame1, self.countryName, self.baseCurrency, self.codeCurrency)
        self.frame3 = Frame3(self, self.bgColor, self.details, self.highlight,
                             self.frame1, self.countryName, self.baseCurrency)
        self.frame4 = Frame4(self, self.bgColor, self.details, self.highlight,
                             self.frame1, self.countryName, self.baseCurrency)

        # set references to the frames within frame1
        self.frame1.setFrames(self.frame1, self.frame2,
                              self.frame3, self.frame4)

        # place frames on the grid
        for frame in (self.frame1, self.frame2, self.frame3, self.frame4):
            frame.grid(row=0, column=0, sticky='nsew')

        # initially display only frame1 and hide the rest
        self.frame1.grid(row=0, column=0, sticky='nsew')
        self.frame2.grid_remove()
        self.frame3.grid_remove()
        self.frame4.grid_remove()


if __name__ == '__main__':
    windll.shcore.SetProcessDpiAwareness(1)

    app = Window()
    app.mainloop()
