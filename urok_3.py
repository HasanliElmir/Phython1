class human:
    def __init__(self, name): #constuctor
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passsengers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers.")
            for passenger in self.passengers:
                print(passenger.name)
            else:
                print("There are no passengers in " + self.brand)


murad = human("Murad shalunishka")
guseyn = human("Chat gptshnik")
elmir = human("Xuliqan")
ulvi = human("Yaxsi oqlan")
jamil = human("Mandarinka")
mika = human("genius millioner")
murad = human("Aliyev aqilli adam")
jalal = human("good player")
melek = human("Strong women")
sulik = human("Suslik")


bmw = Auto("BMW M5")
byd = Auto("BYD")
jiquli = Auto("07")



bmw.add_passenger(murad, melek, mika,murad)
byd.add_passenger(jamil,jalal)
jiquli.add_passenger(guseyn, ulvi, elmir, sulik)

bmw.print_passsengers_names()
byd.print_passsengers_names()
jiquli.print_passsengers_names()
