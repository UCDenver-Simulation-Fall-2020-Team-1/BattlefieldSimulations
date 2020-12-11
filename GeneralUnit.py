from Unit import Unit

class General(Unit):
    def __init__(self, health=11, damage=2, category="General", allegiance=None, initiative=4, accuracy=6, rnge=7, movement=9, evasion=6):
        super(General, self).__init__(health, damage, category, allegiance, initiative, accuracy, rnge, movement, evasion)