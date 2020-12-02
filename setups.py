from Battlefield import *
from Army import *
from Unit import *
import random

def shape_battlefield(x, y, impassible_tiles):
    '''
    Creates an x by y array of Tiles, with the coordinates in impassible_tiles
    set to be impassible

    Arguments:
        - x (positive integer): The width of the array
        - y (positive integer): The height of the array
        - impassible_tiles (array of tuples of two non-negative integers):
          a list of tiles that will be marked as impassible
    
    Returns: A 2D array of the specified width and height, containing tiles
             that are passable except for the tiles indicated by
             impassible_tiles (2 dimensional array of Battlefield.Tiles)
    '''
    passable = [[True for i in range(y)] for j in range(x)]
    for i, j in impassible_tiles:
        passable[i][j] = False
    tiles = [[Battlefield.Tile(passable[j][i], j, i) for i in range(y)] for j in range(x)]
    return tiles

def basic_random_setup(x, y, army_width, army_height = 1):
    '''
    Creates a semi-random starting condition for a battle, with a x by y
    array of tiles. The starting posistions of the units for each Army
    are rectangles that are unit_width by unit_depth.
    Initial positions of the Armies are randomized, however each Army is
    guaranteed to spawn on opposite vertical halves of the battlefield.
    Arguments:
        - x (positive integer): The width of the battlefield
        - y (positive integer): The height of the battlefield
        - army_width (positive integer): the width of the spawn area for each army,
          if army_height is blank, this is instead the number of units per army
        - army_height (positive integer): the height of the spawn area for each army.
          Default value is 1

    Returns: A tuple containing the battlefield array, and the two Armies that
             have been constructed. (2D array of Battlefield.Tiles, Army, Army)
    '''
    tiles = [[Battlefield.Tile(True,j,i) for i in range(y)] for j in range(x)]
    bf = Battlefield(tiles)

    unit_amount = army_width * army_height

    army_one_start_x = (x // 2) - random.randrange(0, army_width)
    army_two_start_x = (x // 2) - random.randrange(0, army_width)

    army_one_start_y = (y // 2) - random.randrange(0, ((y // 2) - army_height))
    army_two_start_y = (y // 2) + army_height + random.randrange(0, ((y // 2) - army_height))

    # generate armies
    u1 = [Unit(50,20,"soldier",1, 5, 0,1,2,0) for i in range(unit_amount)]
    dpl1 = []
    for i in range(army_height):
        dpl1 += [(j+army_one_start_x, i+army_one_start_y) for j in range(army_width)]
    a1 = Army("Army 1",1, u1, dpl1, None)

    u2 = [Unit(50,20,"soldier",2, 5, 0,1,2,0) for i in range(unit_amount)]
    for i in range(army_height):
        dpl2 += [(j+army_two_start_x, i+army_two_start_y) for j in range(army_width)]
    #dpl2 = [(i+army_two_start_x, army_two_start_y) for i in range(unit_amount)]
    a2 = Army("Army 2", 2, u2, dpl2, None)

    return (bf, a1, a2)

def basic_setup(x, y, army1_shape, army2_shape, army1_start, army2_start):
    tiles = [[Battlefield.Tile(True,j,i) for i in range(y)] for j in range(x)]
    bf = Battlefield(tiles)

    unit_amount1 = army1_shape[0]*army1_shape[1]
    unit_amount2 = army2_shape[0]*army2_shape[1]

    army_one_start_x = army1_start[0]
    army_two_start_x = army2_start[0]

    army_one_start_y = army1_start[1]
    army_two_start_y = army2_start[1]

    # generate armies
    u1 = [Unit(50,20,"soldier",1, 5, 0,1,2,0) for i in range(unit_amount1)]
    dpl1 = []
    for i in range(army1_shape[1]):
        dpl1 += [(j+army_one_start_x, i+army_one_start_y) for j in range(army1_shape[0])]
    a1 = Army("Army 1",1, u1, dpl1, None)
    
    u2 = [Unit(50,20,"soldier",2, 5, 0,1,2,0) for i in range(unit_amount2)]
    dpl2 = []
    for i in range(army2_shape[1]):
        dpl2 += [(j+army_two_start_x, i+army_two_start_y) for j in range(army2_shape[0])]
    #dpl2 = [(i+army_two_start_x, army_two_start_y) for i in range(unit_amount)]
    a2 = Army("Army 2", 2, u2, dpl2, None)

    return (bf, a1, a2)

def chokepoint_setup(x, y, army_width, army_height, chokepoint_width):
    '''
    TODO: Description and body
    '''
    pass
