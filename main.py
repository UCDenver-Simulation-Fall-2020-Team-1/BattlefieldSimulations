from Battle import *
from Battlefield import *
from Army import *
from Unit import *

# generate battlefield
tiles = [[Battlefield.Tile(True,j,i) for i in range(10)] for j in range(10)]
bf = Battlefield(tiles)

# generate armies
u1 = [Unit(50,20,"soldier",1, 5, 0,1,2,0) for i in range(4)]
dpl1 = [(i+3,1) for i in range(4)]
a1 = Army("Army 1",2, u1, dpl1, None)

u2 = [Unit(50,20,"soldier",2, 5, 0,1,2,0) for i in range(4)]
dpl2 = [(i+3,8) for i in range(4)]
a2 = Army("Army 2", 2, u2, dpl2, None)

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
for i in range(100)
