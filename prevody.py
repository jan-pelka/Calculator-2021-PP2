import tkinter as tk
from tkinter import ttk
from SolveDelka import *
from SolvePlocha import *
from SolveObjem import *

def prevody(window):
    def delka():

        cisloDelka1 = tk.IntVar()
        ttk.Label(window, text="Délka") .grid(column=0, row=0)
        ttk.Label(window, text="") .grid(column=0, row=1)
        ttk.Label(window, text="prevedeno z") .grid(column=0, row=2)
        ttk.Label(window, text="prevedeno na") .grid(column=4, row=2)
        ttk.Entry(window, width=12, textvariable = cisloDelka1) .grid(column=0,row=3)
        
        JednotkyDelky1=tk.StringVar()
        JednotkyDelky1_chosen=ttk.Combobox(window,width=12,textvariable=JednotkyDelky1)
        JednotkyDelky1_chosen['values'] = ("Palec","Míle","kilometr","metr","centimetr","milimetr")
        JednotkyDelky1_chosen.grid(column=1,row=3)
        JednotkyDelky1_chosen.current(0)

        JednotkyDelky2=tk.StringVar()
        JednotkyDelky2_chosen=ttk.Combobox(window,width=12,textvariable=JednotkyDelky2)
        JednotkyDelky2_chosen['values'] = ("Palec","Míle","kilometr","metr","centimetr","milimetr")
        JednotkyDelky2_chosen.grid(column=4,row=3)
        JednotkyDelky2_chosen.current(0)

        ttk.Label(window, text="=") .grid(column=2, row=3)
        DelkaVystup = ttk.Label(window, text="0") 
        DelkaVystup.grid(column=3, row=3)
        
        ttk.Button(window, text="spočti", command = lambda: Solve_Delka(cisloDelka1,JednotkyDelky1,DelkaVystup,JednotkyDelky2)) .grid(column = 5,row=3)
  
    def plocha():
        cisloPlocha1 = tk.IntVar()
        ttk.Label(window, text="Plocha") .grid(column=0, row=5)
        ttk.Label(window, text="") .grid(column=0, row=6)
        ttk.Label(window, text="prevedeno z") .grid(column=0, row=7)
        ttk.Label(window, text="prevedeno na") .grid(column=4, row=7)
        ttk.Entry(window, width=12, textvariable = cisloPlocha1) .grid(column=0,row=8)
        
        Jednotkyplochy1=tk.StringVar()
        Jednotkyplochy1_chosen=ttk.Combobox(window,width=12,textvariable=Jednotkyplochy1)
        Jednotkyplochy1_chosen['values'] = ("Hektary","Ary","Km^2","m^2","dm^2","cm^2","mm^2")
        Jednotkyplochy1_chosen.grid(column=1,row=8)
        Jednotkyplochy1_chosen.current(0)

        Jednotkyplochy2=tk.StringVar()
        Jednotkyplochy2_chosen=ttk.Combobox(window,width=12,textvariable=Jednotkyplochy2)
        Jednotkyplochy2_chosen['values'] = ("Hektary","Ary","Km^2","m^2","dm^2","cm^2","mm^2")
        Jednotkyplochy2_chosen.grid(column=4,row=8)
        Jednotkyplochy2_chosen.current(0)

        ttk.Label(window, text="=") .grid(column=2, row=8)
        PlochaVystup = ttk.Label(window, text="0") 
        PlochaVystup.grid(column=3, row=8)
        
        ttk.Button(window, text="spočti", command = lambda: Solve_plocha(cisloPlocha1,Jednotkyplochy1,PlochaVystup,Jednotkyplochy2)) .grid(column = 5,row=8)

    def Objem():
        cisloPlocha2 = tk.StringVar()

        ttk.Label(window, text="Délka") .grid(column=0, row=10)
        ttk.Label(window, text="") .grid(column=0, row=11)
        ttk.Label(window, text="prevedeno z") .grid(column=0, row=12)
        ttk.Label(window, text="prevedeno na") .grid(column=4, row=12)
        ttk.Entry(window, width=12, textvariable = cisloPlocha2) .grid(column=0,row=13)
        
        JednotkyObjem1=tk.StringVar()
        JednotkyObjem1_chosen=ttk.Combobox(window,width=12,textvariable=JednotkyObjem1)
        JednotkyObjem1_chosen['values'] = ("km^3","m^3","dm^3","cm^3","mm^3","Litr","Decilitr","Centilitr","Mililitr")
        JednotkyObjem1_chosen.grid(column=1,row=13)
        JednotkyObjem1_chosen.current(0)

        JednotkyObjem2=tk.StringVar()
        JednotkyObjem2_chosen=ttk.Combobox(window,width=12,textvariable=JednotkyObjem2)
        JednotkyObjem2_chosen['values'] = ("km^3","m^3","dm^3","cm^3","mm^3","Litr","Decilitr","Centilitr","Mililitr")
        JednotkyObjem2_chosen.grid(column=4,row=13)
        JednotkyObjem2_chosen.current(0)

        ttk.Label(window, text="=") .grid(column=2, row=13)
        ObjemVystup = ttk.Label(window, text="0") 
        ObjemVystup.grid(column=3, row=13)
        
        ttk.Button(window, text="spočti", command = lambda: Solve_Objem(cisloPlocha2,JednotkyObjem1,ObjemVystup,JednotkyObjem2)) .grid(column = 5,row=13)
    
    
    
    delka()
    ttk.Label(window, text="") .grid(column=0, row=4)
    plocha()
    ttk.Label(window, text="") .grid(column=0, row=9)
    Objem()
    