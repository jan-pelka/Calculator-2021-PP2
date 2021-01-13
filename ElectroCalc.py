import tkinter as tk
from tkinter import ttk

def run_electro(pruh1,pruh2,pruh3,pruh4,pruh5,pruh6,VystupElectro1,VystupElectro2,VystupElectro3):
        
        stovky = str(pruh1.get())
        desitky = str(pruh2.get())
        jednotky = str(pruh3.get())
        násobitel = str(pruh4.get())
        tolerance = str(pruh5.get())
        TeplotníKoeficient = str(pruh6.get())

        Rezistor = 0

        if stovky == "černá":
            Rezistor = "0"
        if stovky == "hnědá":
            Rezistor = "1"
        if stovky == "červená":
            Rezistor = "2"
        if stovky == "oranžová":
            Rezistor = "3"
        if stovky == "žlutá":
            Rezistor = "4"
        if stovky == "zelená":
            Rezistor = "5"
        if stovky == "modrá":
            Rezistor = "6"
        if stovky == "fialová":
            Rezistor = "7"
        if stovky == "šedá":
            Rezistor = "8"
        if stovky == "bílá":
            Rezistor = "9"
        if stovky == "":
            Rezistor = ""

        if desitky == "černá":
            Rezistor = Rezistor + "0"
        if desitky == "hnědá":
            Rezistor = Rezistor + "1"
        if desitky == "červená":
            Rezistor = Rezistor + "2"
        if desitky == "oranžová":
            Rezistor = Rezistor + "3"
        if desitky == "žlutá":
            Rezistor = Rezistor + "4"
        if desitky == "zelená":
            Rezistor = Rezistor + "5"
        if desitky == "modrá":
            Rezistor = Rezistor + "6"
        if desitky == "fialová":
            Rezistor = Rezistor + "7"
        if desitky == "šedá":
            Rezistor = Rezistor + "8"
        if desitky == "bílá":
            Rezistor = Rezistor + "9"

        if jednotky == "černá":
            Rezistor = Rezistor + "0"
        if jednotky == "hnědá":
            Rezistor = Rezistor + "1"
        if jednotky == "červená":
            Rezistor = Rezistor + "2"
        if jednotky == "oranžová":
            Rezistor = Rezistor + "3"
        if jednotky == "žlutá":
            Rezistor = Rezistor + "4"
        if jednotky == "zelená":
            Rezistor = Rezistor + "5"
        if jednotky == "modrá":
            Rezistor = Rezistor + "6"
        if jednotky == "fialová":
            Rezistor = Rezistor + "7"
        if jednotky == "šedá":
            Rezistor = Rezistor + "8"
        if jednotky == "bílá":
            Rezistor = Rezistor + "9"

        if Rezistor == "":
            Rezistor = "0"

        if násobitel == "černá":
            Rezistor = (float(Rezistor))*1
        if násobitel == "hnědá":
            Rezistor = (float(Rezistor))*10
        if násobitel == "červená":
            Rezistor = (float(Rezistor))*100
        if násobitel == "oranžová":
            Rezistor = (float(Rezistor))*1000
        if násobitel == "žlutá":
            Rezistor = (float(Rezistor))*10000
        if násobitel == "zelená":
            Rezistor = (float(Rezistor))*100000
        if násobitel == "modrá":
            Rezistor = (float(Rezistor))*1000000
        if násobitel == "fialová":
            Rezistor = (float(Rezistor))*10000000
        if násobitel == "šedá":
            Rezistor = (float(Rezistor))*100000000
        if násobitel == "bílá":
            Rezistor = (float(Rezistor))*1000000000
        if násobitel == "Zlatá":
            Rezistor = (float(Rezistor))*0.1
        if násobitel == "Stříbrná":
            Rezistor = (float(Rezistor))*0.01

        if float(Rezistor) >= 1000000000000:
            Rezistor = Rezistor/1000000000000
            přípona = " T OHM"
        elif float(Rezistor) >= 1000000000:
            Rezistor = Rezistor/1000000000
            přípona = " G OHM"
        elif float(Rezistor) >= 1000000:
            Rezistor = Rezistor/1000000
            přípona = " M OHM"
        elif float(Rezistor) >= 1000:
            Rezistor = Rezistor/1000
            přípona = " K OHM"
        else:
            přípona = " OHM"

        if tolerance == "hnědá":
            HodnotaTolerance = "+- 1 % (F)"
        if tolerance == "červená":
            HodnotaTolerance = "+- 2 % (G)"
        if tolerance == "zelená":
            HodnotaTolerance = "+- 0,5 % (D)"
        if tolerance == "modrá":
            HodnotaTolerance = "+- 0,025 % (C)"
        if tolerance == "fialová":
            HodnotaTolerance = "+- 0,01 % (B)"
        if tolerance == "šedá":
            HodnotaTolerance = "+- 0,05 % (A)"
        if tolerance == "Zlatá":
            HodnotaTolerance = "+- 5 % (J)"
        if tolerance == "Stříbrná":
            HodnotaTolerance = "+- 10 % (K)"
        if tolerance == "žádná":
            HodnotaTolerance = "+- 20 % (M)"
        if tolerance == "":
            HodnotaTolerance = "NEZADANO"

        if TeplotníKoeficient == "hnědá":
            teplota = "100 ppm"
        if TeplotníKoeficient == "červená":
            teplota = "50 ppm"
        if TeplotníKoeficient == "oranžová":
            teplota = "15 ppm"
        if TeplotníKoeficient == "žlutá":
            teplota = "25 ppm"
        if TeplotníKoeficient == "modrá":
            teplota = "10 ppm"
        if TeplotníKoeficient == "fialová":
            teplota = "5 ppm"
        if TeplotníKoeficient == "bílá":
            teplota = "1 ppm"
        if TeplotníKoeficient == "":
            teplota = "Nezadano"

        VystupElectro1.configure(text = str(Rezistor) + přípona)
        VystupElectro2.configure(text = str(HodnotaTolerance))
        VystupElectro3.configure(text = str(teplota))