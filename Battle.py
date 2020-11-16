# import BattleField
# import Unit
# import Vis

class Battle:
    def __init__(self, battlefield, army1, army2):
        self.battefield = battlefield
        self.army1 = army1
        self.army2 = army2
        self.move_queue = []
        self.turn_number = 0
        self.move_number = 0
        # some debug level?

    def run():
        # drive the simulation, ie, generate move_queues and run through them
        # until an end condition is reached
        # do
        #   move_queue = generate_queue()
        #   for u in move_queue:
        #       take_turn(u)
        #       self.move_number += 1
        #   self.turn_number += 1
        # while not end_condition
        # return end_condition
        pass

    def setup(deployments):
        # put units on battlefield in their deployment zones
        pass

    def take_turn(u):
        # get the move from the unit whose turn it is (or their general)
        # check the move for validity (throw an exception, probably)
        # move_to_string to log file (or use logging class)
        # execute the move (move the unit where it wants to go, and execute the unit's ability)
        # if a unit dies, remove it from the battlefield object, and move_queue
        # generate_frame
        pass

    def apply_move(unit, move):
        # execute the move (move the unit where it wants to go, and execute the unit's ability)
        pass

    def generate_queue():
        # take all (alive) units from both armies, sort by initiative
        # randomize orders within initiatives
        pass

    def end_condition():
        # check for number of turns with no combat, or if all members of an army are dead
        # could return the result
        pass

    def generate_frame():
        # call visualization, maybe some color data, save frame indexed by move number
        pass

