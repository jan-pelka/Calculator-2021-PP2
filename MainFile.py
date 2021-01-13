import tkinter as tk
from tkinter import ttk
import math 
from Calc import basic_graph
from prevody import prevody
from Elektro import graphic_electro

def Run_Calc():

    win = tk.Tk()
    win.title("Calculator jams 211539 211536")
    win.resizable(False, False)
    rows = 0
    while rows < 50:
        win.rowconfigure(rows, weight=1)
        win.columnconfigure(rows, weight=1)
        rows += 1

    nb = ttk.Notebook(win)
    nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

    # Tab 1
    basic = ttk.Frame(nb)
    nb.add(basic, text='basic')
    # filing tab1
    basic_graph(basic)
    #graphic_basic(basic)
 
    # Tab 2
    prevod = ttk.Frame(nb)
    nb.add(prevod, text='prevody')
    # filling tab2
    prevody(prevod)  

    # Tab 3
    electro = ttk.Frame(nb)
    nb.add(electro, text='electro')
    # filling tab3
    graphic_electro(electro)

    win.mainloop()

#jan pelka