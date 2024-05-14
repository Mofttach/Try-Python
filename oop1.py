class Hero(): #template
    #class variable
    jumlah = 0

    def __init__(self, inName, inPower, inHeath, inSpeed):
        #instance variable
        self.Name = inName
        self.Power = inPower
        self.Healt = inHeath
        self.Speed = inSpeed

        Hero.jumlah += 1

        print(f"Telah memebuat Hero {inName} yang merupakan Hero ke {Hero.jumlah}")

Savanna = Hero('Savanna', 10, 10, 9)
Qua = Hero('Qua', 10, 30, 9)