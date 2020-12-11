from Unit import Unit

class Soldier(Unit):
    def __init__(self, health=50, damage=20, category="Soldier", allegiance=None, initiative=5, accuracy=0, rnge=1, movement=2, evasion=0):
        super(Soldier, self).__init__(health, damage, category, allegiance, initiative, accuracy, rnge, movement, evasion)