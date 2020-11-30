class Army:
    def __init__(self, name, num, units, deployment, general):
        self.num = num
        self.name = name
        self.units = units
        self.deployment = deployment
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
        return self.num_alive() == 0

    def num_alive(self):
        return len([u for u in self.units if u.is_alive()])

    def reset(self):
        for u in self.units:
            u.reset()
