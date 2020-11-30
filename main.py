from Battle import *
from Battlefield import *
from Army import *
from Unit import *
from viz import *

## generate battlefield
#tiles = [[Battlefield.Tile(True,j,i) for i in range(10)] for j in range(10)]
#bf = Battlefield(tiles)
#
## generate armies
#u1 = [Unit(50,20,"soldier",1, 5, 0,1,2,0) for i in range(4)]
#dpl1 = [(i+3,1) for i in range(4)]
#a1 = Army("Army 1",2, u1, dpl1, None)
#
#u2 = [Unit(50,20,"soldier",2, 5, 0,1,2,0) for i in range(4)]
#dpl2 = [(i+3,8) for i in range(4)]
#a2 = Army("Army 2", 2, u2, dpl2, None)
#
# assign deployment

# all of above could come from a file (pickled, or json)

## create battle
#btl = Battle(bf, a1, a2)
#btl.setup()
#
## run battle
#winner = btl.run()
#if winner is not None:
#    print(winner.name + " is victorious!")
#else:
#    print("Draw!")

# print result

n = 10
win1 = 0
win2 = 0
draw = 0

board_size = 20
unit_amount = 10

army_one_start_x = 3
army_one_start_y = 1

army_two_start_x = 3
army_two_start_y = 15

viz = game_visualizer(None, None)

for i in range(n):
    # generate battlefield
    tiles = [[Battlefield.Tile(True,j,i) for i in range(board_size)] for j in range(board_size)]
    bf = Battlefield(tiles)

    army_one_start_x = (board_size // 2) - random.randrange(0, unit_amount)
    army_two_start_x = (board_size // 2) - random.randrange(0, unit_amount)

    army_one_start_y = (board_size // 2) - random.randrange(0, (board_size // 2))
    army_two_start_y = (board_size // 2) + random.randrange(0, (board_size // 2))

    # generate armies
    u1 = [Unit(50,20,"soldier",1, 5, 0,1,2,0) for i in range(unit_amount)]
    dpl1 = [(i+army_one_start_x, army_one_start_y) for i in range(unit_amount)]
    a1 = Army("Army 1",1, u1, dpl1, None)
    
    u2 = [Unit(50,20,"soldier",2, 5, 0,1,2,0) for i in range(unit_amount)]
    dpl2 = [(i+army_two_start_x, army_two_start_y) for i in range(unit_amount)]
    a2 = Army("Army 2", 2, u2, dpl2, None)

    viz.board_size = bf._shape[0]
    viz.battlefield = bf
    viz.game_number = i

    battle = Battle(bf, a1, a2, viz)

    battle.setup()
    result = battle.run()

    if result == None:
        draw += 1
    elif result.num == 1:
        win1 += 1
    elif result.num == 2:
        win2 += 1

    viz.army_one_win_count = win1
    viz.army_two_win_count = win2

viz.py_game.quit()

print("Army 1 wins:\t%f" % (float(win1)/n))
print("Army 2 wins:\t%f" % (float(win2)/n))
print("Draws:\t\t%f" % (float(draw)/n))
