import tkinter as tk
from tkinter import ttk

def Solve_plocha(cisloPlocha1,Jednotkyplochy1,PlochaVystup,Jednotkyplochy2):
    cislo1 = float(cisloPlocha1.get())
    jednotka1 = str(Jednotkyplochy1.get())
    jednotka2 = str(Jednotkyplochy2.get())

    #převod vše na metry čtvereční 

    if jednotka1 == "Hektary":
        sidecalc = cislo1*10000
    if jednotka1 == "Ary":
        sidecalc = cislo1*100
    if jednotka1 == "Km^2":
        sidecalc = cislo1*1000000
    if jednotka1 == "m^2":
        sidecalc = cislo1
    if jednotka1 == "dm^2":
        sidecalc = cislo1/100
    if jednotka1 == "cm^2":
        sidecalc = cislo1/10000
    if jednotka1 == "mm^2":
        sidecalc = cislo1/1000000


    # převod na výslednou jednotku

    if jednotka2 == "Hektary":
        cislo2 = sidecalc / 10000
    if jednotka2 == "Ary":
        cislo2 = sidecalc / 100
    if jednotka2 == "Km^2":
        cislo2 = sidecalc / 1000000
    if jednotka2 == "m^2":
        cislo2 = sidecalc
    if jednotka2 == "dm^2":
        cislo2 = sidecalc * 100
    if jednotka2 == "cm^2":
        cislo2 = sidecalc * 10000
    if jednotka2 == "mm^2":
        cislo2 = sidecalc * 1000000

    PlochaVystup.configure(text=cislo2)