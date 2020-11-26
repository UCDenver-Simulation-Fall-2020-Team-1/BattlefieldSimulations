from Battle import *
from Battlefield import *
from Army import *
from Unit import *

# generate battlefield
tiles = [[Battlefield.Tile(True,i,j) for i in range(10)] for j in range(10)]
bf = Battlefield(tiles)

# generate armies
u1 = [Unit(50,20,"soldier","Army 1", 5, 0,0,0,0) for i in range(5)]
dpl1 = [(i+3,1) for i in range(5)]
a1 = Army("Army 1", u1, dpl1, None)

u2 = [Unit(50,20,"soldier","Army 2", 5, 0,0,0,0) for i in range(5)]
dpl2 = [(i+3,8) for i in range(5)]
a2 = Army("Army 2", u2, dpl2, None)

# assign deployment

# all of above could come from a file (pickled, or json)

# create battle
btl = Battle(bf, a1, a2)
btl.setup()

# run battle
btl.run()

# print result
