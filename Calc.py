import tkinter as tk
from tkinter import ttk
from functions import *
from InstantMath import *

def basic_graph(basic):
    MainNumber = tk.StringVar()

    ttk.Label(basic, text="Calculator by jams") .grid(column=0, row=0) #                MAIN LABEL
    ttk.Label(basic, text="in progres") .grid(column=2, row=0) #                   VERSION LABEL

    # Klávesnice rpo obsluhu čísel
    ttk.Button(basic, text="1", command = lambda: add(1,MainNumber)) .grid(column=0, row=2,sticky='W') #              BUTON No. ONE
    ttk.Button(basic, text="2", command = lambda: add(2,MainNumber)) .grid(column=0, row=2) #              BUTON No. TWO
    ttk.Button(basic, text="3", command = lambda: add(3,MainNumber)) .grid(column=0, row=2,sticky='E') #              BUTON No. THREE
    ttk.Button(basic, text="4", command = lambda: add(4,MainNumber)) .grid(column=0, row=3,sticky='W') #              BUTON No. FOUR
    ttk.Button(basic, text="5", command = lambda: add(5,MainNumber)) .grid(column=0, row=3) #              BUTON No. FIVE
    ttk.Button(basic, text="6", command = lambda: add(6,MainNumber)) .grid(column=0, row=3,sticky='E') #              BUTON No. SIX
    ttk.Button(basic, text="7", command = lambda: add(7,MainNumber)) .grid(column=0, row=4,sticky='W') #              BUTON No. SEVEN
    ttk.Button(basic, text="8", command = lambda: add(8,MainNumber)) .grid(column=0, row=4) #              BUTON No. EIGHT
    ttk.Button(basic, text="9", command = lambda: add(9,MainNumber)) .grid(column=0, row=4,sticky='E') #              BUTON No. NINE
    ttk.Button(basic, text="0", command = lambda: add(0,MainNumber)) .grid(column=0, row=5) #              BUTON No. ZERO
    ttk.Button(basic, text=",", command = lambda: add(".",MainNumber)) .grid(column=0, row=5,sticky='W') #          BUTON COMA
    ttk.Button(basic, text="=", command = lambda: solve(MainNumber)) .grid(column=0,row=5,sticky='E') #              SOLVE PROBLEM
    ttk.Button(basic, text="Cscr", command = lambda: Clear_Screen(MainNumber)) .grid(column=0,row=6) #              Reset memory
    ttk.Button(basic, text="Bspc", command = lambda: Go_Back(MainNumber)) .grid(column=0,row=6,sticky='W') #              Reset memory
    

    ttk.Label(basic,text="   ") .grid(column=1,row=3)
    #čudlíky pro funkce vyžadující druhé číslo
    ttk.Label(basic,text="akce vyžaduje druhou číslici") .grid(column=2, row=1)
    ttk.Button(basic, text="+", command = lambda: add("+",MainNumber)) .grid(column=2,row=2,sticky='W')
    ttk.Button(basic, text="-", command = lambda: add("-",MainNumber)) .grid(column=2,row=2,sticky='E')
    ttk.Button(basic, text="*", command = lambda: add("*",MainNumber)) .grid(column=2,row=3,sticky='W')
    ttk.Button(basic, text="/", command = lambda: add("/",MainNumber)) .grid(column=2,row=3,sticky='E')
    ttk.Button(basic, text="^", command = lambda: add("**",MainNumber)) .grid(column=2,row=4,sticky='W')

    #čudlíky fce spuštěné ihned
    ttk.Label(basic,text="akce vyžaduje jednu číslici") .grid(column=2, row=5)
    ttk.Button(basic, text="Sin", command = lambda: Instant_Math_Sin(MainNumber)) .grid(column=2,row=6,sticky='W') #Sinus
    ttk.Button(basic, text="Cos", command = lambda: Instant_Math_Cos(MainNumber)) .grid(column=2,row=6,sticky='E') #Cosinus
    ttk.Button(basic, text="Tg", command = lambda: Instant_Math_Tg(MainNumber)) .grid(column=2,row=7,sticky='W') #Tangens
    ttk.Button(basic, text="x!", command = lambda: Instant_Math_Fact(MainNumber)) .grid(column=2,row=7,sticky='E') #Cotangens
    ttk.Button(basic, text="Log", command = lambda: Instant_Math_log(MainNumber)) .grid(column=2,row=8,sticky='W') #Logaritmus 10
    ttk.Button(basic, text="Ln", command = lambda: Instant_Math_ln(MainNumber)) .grid(column=2,row=8,sticky='E') #Logaritmus e

    

    #deklarace dusplaye
    ttk.Entry(basic, width=12, textvariable = MainNumber, state='disabled') .grid(row=1, ipadx=75) #      pro disabled , state='disabled'

    #ttk.Label(basic, text="LINE CALC") .grid(column=0,row=9)
    #ttk.Entry(basic, width=12) .grid(column=0,row=10)