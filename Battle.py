# import BattleField
# import Unit
# import Vis
import random

class Battle:
    def __init__(self, battlefield, army1, army2):
        self.battlefield = battlefield
        self.army1 = army1
        self.army2 = army2
        self.move_queue = []
        self.turn_number = 0
        self.move_number = 0
        self.turns_since_last_combat = 0
        # some debug level?

    def run(self):
        # drive the simulation, ie, generate move_queues and run through them
        # until an end condition is reached
        while not self.end_condition():
           self.move_queue = self.generate_queue()
           for u in self.move_queue:
               if u.is_alive():
                   self.take_turn(u)
                   self.move_number += 1
           self.turn_number += 1
           self.turns_since_last_combat += 1
        return self.army1 if not self.army1.is_defeated() else self.army2 if not self.army2.is_defeated() else None

    def setup(self):
        # put units on battlefield in their deployment zones
        for i in range(len(self.army1.units)):
            self.battlefield.get_tile(*self.army1.get_deployment()[i]).set_unit(self.army1.get_units()[i])
        for i in range(len(self.army2.units)):
            self.battlefield.get_tile(*self.army2.get_deployment()[i]).set_unit(self.army2.get_units()[i])
        print(self.battlefield)

    def take_turn(self,u):
        # get the move from the unit whose turn it is (or their general)
        print(self.battlefield)
        movement, target = u.get_move(self.battlefield)
        print(str(u.get_id()) + " wants to move with " + str(movement) + " to attack " + str(target) + "\n")
        # check the move for validity (throw an exception, probably)
        # move_to_string to log file (or use logging class)
        # execute the move (move the unit where it wants to go, and execute the unit's ability)
        for move in movement[1:]:
            # move the unit to the new square, remove it from the old
            u.get_tile().remove_unit() 
            self.battlefield.get_tile(*move).set_unit(u)
            print(self.battlefield)
            input("press enter...")
        u.use_ability(self.battlefield.get_tile(*target).unit())
        input("press enter...")
            
            # visualize it, log it
            # print("unit " + str(u.get_id()) + " moved from " + old + " to " + u.get_tile())
        # attack/heal next unit, if possible (set turns_since_last_combat to 0 if it is)
        # 
        # if a unit dies, remove it from the battlefield object, and move_queue 
        # actually probably don't need to worry about the move_queue since it has a check for "alive"
        pass

    def apply_move(self,unit, move):
        # execute the move (move the unit where it wants to go, and execute the unit's ability)
        # probably don't need this function, actually.
        pass

    def generate_queue(self):
        # take all (alive) units from both armies, sort by initiative
        units = [u for u in self.army1.get_units() + self.army2.get_units() if u.is_alive()]
        # order by initiative, and then random
        return sorted(units, key=lambda x: (x.get_initiative(), random.random()))

    def end_condition(self):
        # check for number of turns with no combat, or if all members of an army are dead
        return self.turns_since_last_combat > 10 or self.army1.is_defeated() or self.army2.is_defeated()
        # could return the result
        pass

    def generate_frame(self):
        # call visualization, maybe some color data, save frame indexed by move number
        pass

