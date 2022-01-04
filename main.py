class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("showInfo di class Hero")
        print("{} health: {}".format(self.name,self.health))


class Hero_intelligent(Hero):
    def __init__(self,name,):
        super().__init__(name,100)

    def showInfo(self):
        print("showInfo di subclass Hero_intellegent")
        print("{} \n\tTipe: intelligent, \n\thealth: {}".format(self.name,self.health))


class Hero_strength(Hero):
    def __init__(self,name,):
        super().__init__(name,200)

yesi = Hero_intelligent('yesi')
axe = Hero_strength('axe')

yesi.showInfo()
