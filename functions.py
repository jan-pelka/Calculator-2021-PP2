
def add(a,MainNumber):
    Number = MainNumber.get()
    Number = str(Number) + str(a)
    MainNumber.set(Number)

def Clear_Screen(MainNumber):
    MainNumber.set("")

def Go_Back(MainNumber):
    NewNumber=""
    Number = MainNumber.get()
    Lengh = len(Number)
    for i in range(Lengh-1):
        NewNumber = str(NewNumber) + str(Number[i])
    MainNumber.set(NewNumber)

def solve(MainNumber): #IN PROGRES
	total = str(eval(MainNumber.get())) 
	MainNumber.set(total)

