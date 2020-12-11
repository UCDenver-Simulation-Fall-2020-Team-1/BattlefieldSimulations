from Unit import Unit

class Ranger(Unit):
    def __init__(self, health=35, damage=15, category="Ranger", allegiance=None, initiative=5, accuracy=0, rnge=3, movement=1, evasion=0):
        super(Ranger, self).__init__(health, damage, category, allegiance, initiative, accuracy, rnge, movement, evasion)