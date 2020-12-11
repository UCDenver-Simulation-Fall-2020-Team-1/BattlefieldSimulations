from Unit import Unit

class Healer(Unit):
    def __init__(self, health=50, damage=20, category="Healer", allegiance=None, initiative=5, accuracy=0, rnge=1, movement=1, evasion=0):
        super(Healer, self).__init__(health, damage, category, allegiance, initiative, accuracy, rnge, movement, evasion)