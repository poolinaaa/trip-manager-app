import customtkinter
from tkinter import *

#customtkinter.set_appearance_mode("System")
#customtkinter.set_default_color_theme("blue")

app = Tk()  # create window
app.geometry("400x240")

def button_callback():
    print("button pressed")

# create button
button = customtkinter.CTkButton(app, command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()