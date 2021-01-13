import tkinter as tk
from tkinter import ttk
from ElectroCalc import run_electro


def graphic_electro(electro):

    pruh1=tk.StringVar()
    pruh1_chosen=ttk.Combobox(electro,width=12,textvariable=pruh1)
    pruh1_chosen['values'] = ("","černá","hnědá","červená","oranžová","žlutá","zelená","modrá","fialová","šedá","bílá")
    pruh1_chosen.grid(column=0,row=2)
    pruh1_chosen.current(0)
        
    pruh2=tk.StringVar()
    pruh2_chosen=ttk.Combobox(electro,width=12,textvariable=pruh2)
    pruh2_chosen['values'] = ("","černá","hnědá","červená","oranžová","žlutá","zelená","modrá","fialová","šedá","bílá")
    pruh2_chosen.grid(column=1,row=2)
    pruh2_chosen.current(0)
        
    pruh3=tk.StringVar()
    pruh3_chosen=ttk.Combobox(electro,width=12,textvariable=pruh3)
    pruh3_chosen['values'] = ("","černá","hnědá","červená","oranžová","žlutá","zelená","modrá","fialová","šedá","bílá")
    pruh3_chosen.grid(column=2,row=2)
    pruh3_chosen.current(0)

    pruh4=tk.StringVar()
    pruh4_chosen=ttk.Combobox(electro,width=12,textvariable=pruh4)
    pruh4_chosen['values'] = ("","černá","hnědá","červená","oranžová","žlutá","zelená","modrá","fialová","šedá","bílá","Zlatá","Stříbrná")
    pruh4_chosen.grid(column=3,row=2)
    pruh4_chosen.current(0)

    pruh5=tk.StringVar()
    pruh5_chosen=ttk.Combobox(electro,width=12,textvariable=pruh5)
    pruh5_chosen['values'] = ("","hnědá","červená","zelená","modrá","fialová","šedá","Zlatá","Stříbrná","žádná")
    pruh5_chosen.grid(column=4,row=2)
    pruh5_chosen.current(0)
    
    pruh6=tk.StringVar()
    pruh6_chosen=ttk.Combobox(electro,width=12,textvariable=pruh6)
    pruh6_chosen['values'] = ("","hnědá","červená","oranžová","žlutá","modrá","fialová","bílá")
    pruh6_chosen.grid(column=5,row=2)
    pruh6_chosen.current(0)
        

    ttk.Label(electro, text="Značení odporů") .grid(column=0, row=0)
    ttk.Label(electro, text="OK1TVL") .grid(column=6, row=0)
    ttk.Label(electro, text="1.pruh") .grid(column=0, row=1)
    ttk.Label(electro, text="2.pruh") .grid(column=1, row=1)
    ttk.Label(electro, text="3.pruh") .grid(column=2, row=1)
    ttk.Label(electro, text="Násobitel") .grid(column=3, row=1)
    ttk.Label(electro, text="Tolerance") .grid(column=4, row=1)
    ttk.Label(electro, text="Tepl koeficient") .grid(column=5, row=1)

    Odpor = ttk.Labelframe(electro, text="ODPOR") 
    Odpor.grid(column=2, row=3, padx=20, pady=30)

    VystupElectro1 = ttk.Label(Odpor, text="0 OHM") 
    VystupElectro1.grid(column=0,row=0)

    VystupElectro2 = ttk.Label(Odpor, text="0% TOL") 
    VystupElectro2.grid(column=0,row=1)

    VystupElectro3 = ttk.Label(Odpor, text="0 PPM") 
    VystupElectro3.grid(column=0,row=2)

    ttk.Button(electro, text="vypočti", command = lambda: run_electro(pruh1,pruh2,pruh3,pruh4,pruh5,pruh6,VystupElectro1,VystupElectro2,VystupElectro3)) .grid(column=2, row=4)  #POZOR NEVOLA FCI