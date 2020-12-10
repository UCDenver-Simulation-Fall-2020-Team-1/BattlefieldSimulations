# import BattleField
# import Unit
from datetime import datetime
import random
from viz import game_visualizer
import time



class Battle:
    def __init__(self, battlefield, army1, army2, game_view, desc="battle", generate_frames=False):
        self.battlefield = battlefield
        self.army1 = army1
        self.army2 = army2
        self.move_queue = []
        self.turn_number = 0
        self.move_number = 0
        self.turns_since_last_combat = 0
        self.desc = desc + "_" + str(datetime.now().strftime("%m-%d_%H:%M:%S"))
        self.frame_title = self.desc + "_" + "turn%03d" + "_" + "move%03d" +  ".png"
        self.viz = game_view

    def run(self):
        # drive the simulation, ie, generate move_queues and run through them
        # until an end condition is reached
        viz_game_exit = False
        while not viz_game_exit:
            while not self.end_condition():
                self.move_queue = self.generate_queue()
                for u in self.move_queue:
                    if u.is_alive():
                        self.take_turn(u)
                        self.move_number += 1

                        if self.viz != None:
                            self.viz.update_board(self.battlefield)
                            time.sleep(0.0001)

                self.turn_number += 1
                self.move_number = 0
                self.turns_since_last_combat += 1
            
            if self.viz != None:
                viz_game_exit = self.viz.game_exit
            else:
                viz_game_exit = True

            return self.army1 if not self.army1.is_defeated() else self.army2 if not self.army2.is_defeated() else None

    def setup(self):

        if self.viz != None:
            self.viz.battlefield = self.battlefield
            self.viz.board_size = self.battlefield._shape[0]

            self.viz.start()

        # put units on battlefield in their deployment zones
        for i in range(len(self.army1.units)):
            self.battlefield.get_tile(*self.army1.get_deployment()[i]).set_unit(self.army1.get_units()[i])
        for i in range(len(self.army2.units)):
            self.battlefield.get_tile(*self.army2.get_deployment()[i]).set_unit(self.army2.get_units()[i])
        self.turn_number +=1

        #print(self.battlefield)

    def take_turn(self,u):
        # get the move from the unit whose turn it is (or their general)
        # print(self.battlefield)
        movement, target = u.get_move(self.battlefield)
        # print(str(u.get_id()) + " wants to move with " + str(movement) + " to attack " + str(target) + "\n")
        # execute the move (move the unit where it wants to go, and execute the unit's ability)
        if movement != None:
            for move in movement[1:]:
                # move the unit to the new square, remove it from the old
                u.get_tile().remove_unit() 
                self.battlefield.get_tile(*move).set_unit(u)
                #print(self.battlefield)
                #input("press enter...")
        if target != None:
            u.use_ability(self.battlefield.get_tile(*target).unit())
        #input("press enter...")

    def generate_queue(self):
        # take all (alive) units from both armies, sort by initiative
        units = [u for u in self.army1.get_units() + self.army2.get_units() if u.is_alive()]
        # order by initiative, and then random
        return sorted(units, key=lambda x: (x.get_initiative(), random.random()))

    def end_condition(self):
        # check for number of turns with no combat, or if all members of an army are dead
        return self.turns_since_last_combat > 10 or self.army1.is_defeated() or self.army2.is_defeated()

    def reset(self):
        self.army1.reset()
        self.army2.reset()
        self.battlefield.reset()

        self.move_queue = []
        self.turn_number = 0
        self.move_number = 0
        self.turns_since_last_combat = 0

        self.setup()
