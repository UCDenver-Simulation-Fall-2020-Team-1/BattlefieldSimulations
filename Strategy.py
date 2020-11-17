# Quinn Owens

from collections import deque

# Copy/paste into Soldier child class (of Unit)
def soldier_strategy(self, battlefield):
    """

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

    """
    #move = array, (up/down/left/right, up/down/left/right)
    #target = array, (coordianates of target)

    path = bfs(battlefield, lambda x: x.allegiance == self.allegiance)
    move = path[:self.movement]
    target = [-1]
    return (move, target)

# Copy/paste into Unit parent class
def bfs(self, battlefield, is_valid_target):
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