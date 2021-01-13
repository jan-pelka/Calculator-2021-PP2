import math

def Instant_Math_Sin(MainNumber):
    Number = MainNumber.get()
    Number = float(Number)
    Number = math.sin(Number)
    Number = str(Number)
    MainNumber.set(Number)

def Instant_Math_Cos(MainNumber):
    Number = MainNumber.get()
    Number = float(Number)
    Number = math.cos(Number)
    Number = str(Number)
    MainNumber.set(Number)

def Instant_Math_Tg(MainNumber):
    Number = MainNumber.get()
    Number = float(Number)
    Number = math.tan(Number)
    Number = str(Number)
    MainNumber.set(Number)

def Instant_Math_Fact(MainNumber):
    Number = MainNumber.get()
    Number = float(Number)
    Number = math.factorial(Number)
    Number = str(Number)
    MainNumber.set(Number)

def Instant_Math_log(MainNumber):
    Number = MainNumber.get()
    Number = float(Number)
    Number = math.log10(Number)
    Number = str(Number)
    MainNumber.set(Number)

def Instant_Math_ln(MainNumber):
    Number = MainNumber.get()
    Number = float(Number)
    Number = math.log(Number)
    Number = str(Number)
    MainNumber.set(Number)
