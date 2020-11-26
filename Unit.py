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

    def __init__(self, health,damage, category, allegiance, initiative, accuracy, rnge, movement, evasion):
        self.health = health
        self.health_max = health
        self.damage = damage
        self.category = category
        self.allegiance = allegiance
        self.initiative = initiative
        self.accuracy = accuracy
        self.range = rnge
        self.movement = movement
        self.evasion = evasion


    #getters
    def get_health(self):
        return self.health
    def get_damage(self):
        return self.damage
    def get_catagory(self):
        return self.catagory
    def get_armytype(self):
        return self.armytype
    def get_initiative(self):
        return self.initiative
    def get_accuracy(self):
        return self.accuracy
    def get_range(self):
        return self.range
    def get_movement(self):
        return self.movement
    def get_evasion(self):
        return self.evasion


    def set_health(self, health):
        self.health = health
    def set_damage(self, damage):
        self.damage = damage
    def set_catagory(self, catagory):
        self.catagory = catagory
    def set_initiative(self, initiative):
        self.initiative = initiative
    def set_accuracy(self, accuracy):
        self.accuracy = accuracy
    def set_range(self, range):
        self.range = range
    def set_movement(self,movement):
        self.movement = movement
    def set_evasion(self, evasion):
        self.evasion = evasion

    def is_alive():
        return self.health != 0
    def harm(num):
        self.health -= num
        if self.health < 0:
            self.health = 0
    def heal(num):
        self.health += num
        if self.health > self.health_max:
            self.health = self.health_max

#a = Unit(11,2, "skdfh", "sdjfg", 4, 6, 7, 9, 3)
#print(a.get_damage())
#a.set_damage(67)
#print(a.get_damage())






