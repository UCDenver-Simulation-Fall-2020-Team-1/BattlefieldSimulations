class Unit:


    # Class(Sharvita)

    # Hit Points(HP)
    # Damage
    # Movement speed
    # Range
    # Accuracy
    # Initiative
    # Unit category & type
    # Initiative
    # Unit category & type

    # Evasion
    # Abilities

    movementspeed = 0
    health = 0
    damage = 0
    catagory = ""
    armytype = ""
    initiative = 0
    accuracy = 0
    range = 0
    abilities = ""
    evasion = 0
    armytype = ""


    def __init__(self, health,damage, catagory, armytype, initiative, accuracy, range, movementspeed, evasion):
        self._healthPoint = health
        self._damage = damage
        self._catagory = catagory
        self._armytype = armytype
        self._initiative = initiative
        self._accuracy = accuracy
        self._range = range
        self._movementspeed = movementspeed
        self._evasion = evasion


    #getters
    def gethealth(self):
        return self._health
    def getdamage(self):
        return self._damage
    def getcatagory(self):
        return self._catagory
    def getarmytype(self):
        return self._armytype
    def getinitiative(self):
        return self._initiative
    def getaccuracy(self):
        return self._accuracy
    def getrange(self):
        return self._range
    def getmovementspeed(self):
        return self._movementspeed
    def getevasion(self):
        return self._evasion


    #setter
    def sethealth(self, health):
        self._health = health
    def setdamage(self, damage):
        self._damage = damage
    def setcatagory(self, catagory):
        self._catagory = catagory
    def setinitiative(self, initiative):
        self._initiative = initiative
    def setaccuracy(self, accuracy):
        self._accuracy = accuracy
    def setrange(self, range):
        self._range = range
    def setmovementspeed(self,movementspeed):
        self._movementspeed = movementspeed
    def setevasion(self, evasion):
        self._evasion = evasion

#a = Unit(11,2, "skdfh", "sdjfg", 4, 6, 7, 9, 3)
#print(a.getdamage())
#a.setdamage(67)
#print(a.getdamage())






