from Battlefield import *
from Army import *
from Unit import *
import random

def shape_battlefield(x, y, impassible_tiles = []):
    '''
    Creates an x by y array of Tiles, with the coordinates in impassible_tiles
    set to be impassible

    Arguments:
        - x (positive integer): The width of the array
        - y (positive integer): The height of the array
        - impassible_tiles (array of tuples of two non-negative integers):
          a list of tiles' coordinates that will be marked as impassible
          Default value is an empty array
    
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
    bf = Battlefield(shape_battlefield(x, y))

    x_mid = x // 2
    y_mid = y // 2

    # Generate army's coordinates
    unit_amount = army_width * army_height
    army_one_start_x = random.randrange(x - army_width)
    army_two_start_x = random.randrange(x - army_width)
    army_one_start_y = random.randrange(y_mid - army_height)
    army_two_start_y = random.randrange(y_mid, y - army_height)

    # generate armies
    u1 = [Unit(50,20,"soldier",1, 5, 0,1,2,0) for i in range(unit_amount)]
    dpl1 = []
    for i in range(army_height):
        dpl1 += [(j+army_one_start_x, i+army_one_start_y) for j in range(army_width)]
    a1 = Army("Army 1",1, u1, dpl1, None)
    # Army 2
    u2 = [Unit(50,20,"soldier",2, 5, 0,1,2,0) for i in range(unit_amount)]
    dpl2 = []
    for i in range(army_height):
        dpl2 += [(j+army_two_start_x, i+army_two_start_y) for j in range(army_width)]
    a2 = Army("Army 2", 2, u2, dpl2, None)

    return (bf, a1, a2)

def chokepoint_setup(x, y, army_width, cp_width, army_height = 1, cp_wall_height = 1):
    '''
    Functions as basic_random_setup(), but creates a map that is split in two,
    with a small pathway between the halves (a chokepoint)

    Arguments:
        - x (positive integer): The width of the battlefield
        - y (positive integer): The height of the battlefield
        - army_width (positive integer): the width of the spawn area for each army,
          if army_height is blank, this is instead the number of units per army
        - cp_width (positive integer): the width of the opening in the center wall
        - army_height (positive integer): the height of the spawn area for each army.
          Default value is 1
        - cp_wall_height (positive integer): the height of the center wall. Default
          value is 1
    
    Returns: A tuple containing the battlefield array, and the two Armies that
             have been constructed. (2D array of Battlefield.Tiles, Army, Army)
    '''
    # Calculate information regarding the center wall
    x_mid = x // 2
    y_mid = y // 2
    # Start x and end x of the chokepoint
    cp_x1 = x_mid - cp_width // 2
    cp_x2 = cp_x1 + cp_width
    # Start y and end y of the chokepoint's wall
    cp_y1 = y_mid - cp_wall_height // 2
    cp_y2 = cp_y1 + cp_wall_height
    
    # Generate list of all the impassable tiles
    impassable = []
    for i in range(cp_y1, cp_y2):
        for j in range(cp_x1):
            impassable += [(j, i)]
        for j in range(cp_x2, x):
            impassable += [(j, i)]
    
    # Generate battlefield map
    bf = Battlefield(shape_battlefield(x, y, impassable))

    # Generate army's coordinates
    unit_amount = army_width * army_height
    army_one_start_x = random.randrange(x - army_width)
    army_two_start_x = random.randrange(x - army_width)
    army_one_start_y = random.randrange(cp_y1 - army_height)
    army_two_start_y = random.randrange(cp_y2, y - army_height)

    # generate armies
    u1 = [Unit(50,20,"soldier",1, 5, 0,1,2,0) for i in range(unit_amount)]
    dpl1 = []
    for i in range(army_height):
        dpl1 += [(j+army_one_start_x, i+army_one_start_y) for j in range(army_width)]
    a1 = Army("Army 1",1, u1, dpl1, None)
    # Army 2
    u2 = [Unit(50,20,"soldier",2, 5, 0,1,2,0) for i in range(unit_amount)]
    dpl2 = []
    for i in range(army_height):
        dpl2 += [(j+army_two_start_x, i+army_two_start_y) for j in range(army_width)]
    a2 = Army("Army 2", 2, u2, dpl2, None)

    return (bf, a1, a2)

def triangles_setup(x, y, triangle_base):
    '''
    Functions as basic_random_setup(), but spawns the armies in two triangle
    formations. The triangles point towards the other side of the battlefield, 
    and on each level of the triangle, there are two less units than the previous
    level (one less unit on each side).

    Arguments:
        - x (positive integer): The width of the battlefield
        - y (positive integer): The height of the battlefield
        - triangle_base (positive integer): The length of the base of the triangle;
          height is calculated automatically.
    '''
    bf = Battlefield(shape_battlefield(x, y))

    triangle_height = triangle_base // 2 + triangle_base % 2
    x_mid = x // 2
    y_mid = y // 2

    # Generate army's coordinates
    army_one_start_x = random.randrange(x - triangle_base)
    army_two_start_x = random.randrange(x - triangle_base)
    army_one_start_y = random.randrange(y_mid - triangle_height)
    army_two_start_y = random.randrange(y_mid, y - triangle_height)

    # Generate armies
    # Army 1
    u1 = []
    dp1 = []
    width = triangle_base
    offset = 0
    for i in range(triangle_height):
        for j in range(width):
            u1 += [Unit(50,20,"soldier",1, 5, 0,1,2,0)]
            ux = army_one_start_x + offset + j
            uy = army_one_start_y + i
            dp1 += [(ux, uy)]
        # At each level increase the offset and decrease the width
        width -= 2
        offset += 1
    a1 = Army("Army 1",1, u1, dpl1, None)
    # Army 2
    u2 = []
    dp2 = []
    if triangle_base % 2 == 0:
        width = 2
    else:
        width = 1
    offset = triangle_base // 2 - 1 + (triangle_base % 2)
    for i in range(triangle_height):
        for j in range(width):
            u1 += [Unit(50,20,"soldier",1, 5, 0,1,2,0)]
            ux = army_one_start_x + offset + j
            uy = army_one_start_y + i
            dp1 += [(ux, uy)]
        # At each leve decrease the offest and increase the width
        width += 2
        offset -= 1
    a2 = Army("Army 2", 2, u2, dpl2, None)

    return (bf, a1, a2)