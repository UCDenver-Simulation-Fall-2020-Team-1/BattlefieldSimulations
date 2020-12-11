from collections import deque

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
    id_gen = 1

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
        self.id = Unit.id_gen
        Unit.id_gen += 1
        self.tile = None

    #getters
    def get_health(self):
        return self.health
    def get_health_max(self):
        return self.health_max
    def get_damage(self):
        return self.damage
    def get_category(self):
        return self.category
    def get_allegiance(self):
        return self.allegiance
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
    def get_tile(self):
        return self.tile
    def get_id(self):
        return self.id

    def set_health(self, health):
        self.health = health
    def set_damage(self, damage):
        self.damage = damage
    def set_category(self, category):
        self.category = category
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
    def set_tile(self, tile):
        self.tile = tile

    def reset(self):
        self.health = self.health_max

    def is_alive(self):
        return self.health != 0
    def harm(self, num):
        self.health -= num
        if self.health < 0:
            self.health = 0
            self.tile.remove_unit()
            self.tile = None
            #print(str(self.id) + " has died")
        else:
            """"""
            #print(str(self.id) + " has " + str(self.health))
    def heal(self, num):
        self.health += num
        if self.health > self.health_max:
            self.health = self.health_max
    def use_ability(self, target_unit):
        self.soldier_use_ability(target_unit)
    def target_in_range(self, target_unit):
        pos = self.get_tile().coors()
        tpos = target_unit.get_tile().coors()
        dist = abs(pos[0]-tpos[0]) + abs(pos[1]-tpos[1])
        return dist <= self.range
    def get_move(self, battlefield):
        return self.soldier_strategy(battlefield)

    def bfs(self, battlefield, is_valid_target):
        """
        Every unit scans the battlefield for a valid target using a breadth-first search, finding a path to them
        in order to use their ability on them.
        self = Self
        battlefield = the 2D array that stores all of the battlefield tiles
        is_valid_target = determines if the unit will target friendly or enemy units
        """
        queue = deque([[self.tile.coors()]])
        seen = set(self.tile.coors())
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if battlefield.get_tile(x,y).has_unit() and is_valid_target(battlefield.get_tile(x,y).unit()):
                return path
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                #print(x2,y2,battlefield.get_tile(x2,y2).is_passable())
                if 0 <= x2 < battlefield.shape()[0] and 0 <= y2 < battlefield.shape()[1]:
                    t = battlefield.get_tile(x2,y2)
                    if (t.is_passable() or (t.has_unit() and is_valid_target(t.unit()))) and (x2, y2) not in seen:
                        queue.append(path + [(x2, y2)])
                        seen.add((x2, y2))

    def soldier_strategy(self, battlefield):
        """
        Scans the battlefield using bfs() for a target it can attack adjacently.
        self = Self
        battlefield = the 2D array that stores all of the battlefield tiles
        """
        #move = array, (up/down/left/right, up/down/left/right)
        #target = array, (coordianates of target)
    
        path = self.bfs(battlefield, lambda x: x.allegiance != self.allegiance)
        if path == None:
            #print(str(self.id) + " is stuck")
            return (None,None)
        if len(path) - 2 < self.movement:
            move = path[:-1]
        else:
            move = path[:self.movement+1]
        target = path[-1]
        return (move, target)

    def soldier_use_ability(self, target_unit):
        if not self.target_in_range(target_unit):
            #print(str(self.id) + " can't reach " + str(target_unit.get_id()))
            return
        #print(str(self.id) + " swings on " + str(target_unit.get_id()) + " for " + str(self.damage) + " damage")
        target_unit.harm(self.damage)
