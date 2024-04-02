# import customtkinter
# from tkinter import *
# from tkinter import ttk
# import tkinter as tk
# from tkinter import messagebox
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import database

# app = customtkinter.CTk()
# app.title('INVENTORY MANAGEMENT SYSTEM')
# app.geometry('800x680')
# app.config(bg='#0A0D0C')
# app.resizable(TRUE,TRUE)

# font1 = ('Arial',25,'bold')

# app.mainloop()

import tkinter as Tk
from tkinter import *


master=Tk()

master.title('INVENTORY MANAGEMENT SYSTEM')
master.geometry('1080x680')
master.config(bg='#0A0D0C')

# master.Label(text="Enter Name").pack()
# master.Entry().pack()


b1=Button(master,text = "SUBMIT")
b1.place(relx = 0.5, rely = 0.5, anchor = CENTER)


master.mainloop()