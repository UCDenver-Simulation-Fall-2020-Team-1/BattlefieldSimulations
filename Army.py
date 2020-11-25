

class Army:
    def __init__(self, name, units, deployment, general):
        self.name = name
        self.units = units
        self.deployment = deployment
        self.units_alive = len(units)
        self.general = general

    def get_name(self):
        return self.name

    def get_units(self):
        return self.units

    def get_deployment(self):
        return self.deployment

    def get_general(self):
        return self.general

    def is_defeated(self):
        return self.units_alive == 0

    def num_alive(self):
        return self.units_alive

    def unit_died(self):
        self.units_alive -= 1
