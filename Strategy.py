# Quinn Owens

from collections import deque

# Copy/paste into Soldier child class (of Unit)
def soldier_strategy(self, battlefield):
    """
    Scans the battlefield using bfs() for a target it can attack adjacently.
    self = Self
    battlefield = the 2D array that stores all of the battlefield tiles
    """
    #move = array, (up/down/left/right, up/down/left/right)
    #target = array, (coordianates of target)

    path = bfs(battlefield, lambda x: x.allegiance != self.allegiance)
    move = path[:self.movement]
    target = [-1]
    return (move, target)

# Copy/paste into Healer child class (of Unit)
def healer_strategy(self, battlefield):
    """
    Scans the battlefield using bfs() for a target it can heal adjacently.
    self = Self
    battlefield = the 2D array that stores all of the battlefield tiles
    """
    #move = array, (up/down/left/right, up/down/left/right)
    #target = array, (coordianates of target)

    path = bfs(battlefield, lambda x: x.allegiance == self.allegiance)
    move = path[:self.movement]
    target = [-1]
    return (move, target)

# Copy/paste into Healer child class (of Unit)
def ranger_strategy(self, battlefield):
    """
    Scans the battlefield using bfs() for a target it can attack from a range.
    self = Self
    battlefield = the 2D array that stores all of the battlefield tiles
    """
    #move = array, (up/down/left/right, up/down/left/right)
    #target = array, (coordianates of target)

    path = bfs(battlefield, lambda x: x.allegiance != self.allegiance)
    if(len(path) > 5): #replace 5 with self.range, if it is recorded in the ranger's stats
        move = path[:self.movement]
    else:
        move = path[:0]
    target = [-1]
    return (move, target)

# Copy/paste into Healer child class (of Unit)
def general_strategy(self, battlefield):
    """
    Scans the battlefield using bfs() for a target it can attack adjacently.
    self = Self
    battlefield = the 2D array that stores all of the battlefield tiles
    """
    #move = array, (up/down/left/right, up/down/left/right)
    #target = array, (coordianates of target)

    path = bfs(battlefield, lambda x: x.allegiance != self.allegiance)
    move = path[:self.movement]
    target = [-1]
    return (move, target)

# Copy/paste into Unit parent class
def bfs(self, battlefield, is_valid_target):
    """
    Every unit scans the battlefield for a valid target using a breadth-first search, finding a path to them
    in order to use their ability on them.
    self = Self
    battlefield = the 2D array that stores all of the battlefield tiles
    is_valid_target = determines if the unit will target friendly or enemy units
    """
    queue = deque([[self.position]])
    seen = self.position
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if is_valid_target(battlefield.get_tile(x,y).unit()):
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < battlefield.get_width() and 0 <= y2 < battlefield.get_height() \
                    and battlefield.get_tile(x,y).is_passable() and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))