import tkinter as tk
from tkinter import ttk

def Solve_Delka(cisloDelka1,JednotkyDelky1,DelkaVystup,JednotkyDelky2):
    cislo1 = float(cisloDelka1.get())
    jednotka1 = str(JednotkyDelky1.get())
    jednotka2 = str(JednotkyDelky2.get())

    #převod vše na metry

    if jednotka1 == "Palec":
        sidecalc = (cislo1*2.54)/100
    if jednotka1 == "Míle":
        sidecalc = (cislo1*1.609344)*1000
    if jednotka1 == "kilometr":
        sidecalc = (cislo1*1)*1000
    if jednotka1 == "metr":
        sidecalc = (cislo1*1)/1
    if jednotka1 == "centimetr":
        sidecalc = (cislo1/100)/1
    if jednotka1 == "milimetr":
        sidecalc = (cislo1/1000)/1

    # převod na výslednou jednotku

    if jednotka2 == "Palec":
        cislo2 = (sidecalc*100)/2.54
    if jednotka2 == "Míle":
        cislo2 = (sidecalc/1000)/1.609344
    if jednotka2 == "kilometr":
        cislo2 = (sidecalc/1000)/1
    if jednotka2 == "metr":
        cislo2 = (sidecalc*1)/1
    if jednotka2 == "centimrtr":
        cislo2 = (sidecalc*100)/1
    if jednotka2 == "milimetr":
        cislo2 = (sidecalc*1000)/1

    DelkaVystup.configure(text=str(cislo2))