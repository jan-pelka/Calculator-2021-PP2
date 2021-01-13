import tkinter as tk
from tkinter import ttk

def Solve_Objem(cisloObjem1,JednotkyObjem1,ObjemVystup,JednotkyObjem2):
    
    #    "km^3","m^3","dm^3","cm^3","mm^3","Litr","Decilitr","Centilitr","Mililitr"

    cislo1 = float(cisloObjem1.get())
    jednotka1 = str(JednotkyObjem1.get())
    jednotka2 = str(JednotkyObjem2.get())

    #převod vše na metry krychlové 

    if jednotka1 == "km^3":
        sidecalc = cislo1 * 1000000000
    if jednotka1 == "m^3":
        sidecalc = cislo1
    if jednotka1 == "dm^3":
        sidecalc = cislo1 / 1000
    if jednotka1 == "cm^3":
        sidecalc = cislo1 / 1000000
    if jednotka1 == "mm^3":
        sidecalc = cislo1 / 1000000000
    if jednotka1 == "Litr":
        sidecalc = cislo1 / 1000
    if jednotka1 == "Decilitr":
        sidecalc = cislo1 / 10000
    if jednotka1 == "Centilitr":
        sidecalc = cislo1 / 100000
    if jednotka1 == "Mililitr":
        sidecalc = cislo1 / 1000000


    if jednotka2 == "km^3":
        cislo2 = sidecalc / 1000000000
    if jednotka2 == "m^3":
        cislo2 = sidecalc
    if jednotka2 == "dm^3":
        cislo2 = sidecalc * 1000
    if jednotka2 == "cm^3":
        cislo2 = sidecalc * 1000000
    if jednotka2 == "mm^3":
        cislo2 = sidecalc * 1000000000
    if jednotka2 == "Litr":
        cislo2 = sidecalc * 1000
    if jednotka2 == "Decilitr":
        cislo2 = sidecalc * 10000
    if jednotka2 == "Centilitr":
        cislo2 = sidecalc * 100000
    if jednotka2 == "Mililitr":
        cislo2 = sidecalc * 1000000


    ObjemVystup.configure(text=cislo2)