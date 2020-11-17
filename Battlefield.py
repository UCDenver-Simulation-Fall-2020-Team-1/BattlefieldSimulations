class Battlefield:
    '''
    TODO: Description
    '''
    class Tile:
        '''
        Currently only holds information about whether or not the tile is passable,
        coordinates of the tile and a reference to a unit that is on the tile (if there 
        is one)
        Possibly add movement modifiers, etc later

        TODO: Actual Description & Possible Additional Modifiers
        '''
        def __init__(self, passable, x, y, unit = None):
            '''
            TODO: Description
            '''
            self._passable = passable
            self._coors = (x,y)
            self._unit = unit
        def is_passable(self):
            '''
            Returns whether or not the tile is passable
            Returns: True when the tile is passable and False if not (bool)
            '''
            # Currently, tile is impassable if there is a unit on it
            if self._unit is not None:
                return False
            return self._passable
        def x(self):
            '''
            Returns the y coordinate of the Tile
            Returns: The y coordinate (non-negative int)
            '''
            return self._coors[0]
        def y(self):
            '''
            Returns the y coordinate of the Tile
            Returns: The y coordinate (non-negative int)
            '''
            return self._coors[1]
        def coors(self):
            '''
            Returns a tuple containing the x, y coordinates
            Returns: A tuple containing the x, y coordinates (non-negative int, non-negative int)
            '''
            return self._coors
        def unit(self):
            '''
            Returns the Unit on the tile or None if there is none
            Returns: The Unit on this tile (subclass of UnitParent) or None (NoneType) if there is none
            '''
            return self._unit
        def set_unit(self, unit):
            '''
            Sets the unit on this tile

            Arguments:
                unit (subclass of UnitParent): the unit to put on this tile
            
            Returns: The unit that was previously on this Tile (subclass of UnitParent) or None (NoneType)
                     if the tile was empty
            '''
            old_unit = self._unit
            self._unit = unit
            return old_unit
        def remove_unit(self):
            '''
            Removes the unit on this tile. Identical to set_unit(None)

            Returns: The unit that was previously on this Tile (subclass of UnitParent) or None (NoneType)
                     if the tile was empty
            '''
            return self.set_unit(None)

        def has_unit(self):
            '''
            Returns whether or not there is a Unit on this tile
            Returns: True if there is a Unit on this tile, False if not (bool)
            '''
            return self._unit is not None

    def __init__(self, x, y):
        '''
        TODO: Description & body
        '''
        pass

    def get_tile(self, x, y):
        '''
        Returns the Tile object at (x, y)

        Args:
            x - the x coordinate of the Tile (non-negative int)
            y - the y coordinate of the Tile (non-negative int)
        
        Returns: The Tile object at (x, y) (class Tile)

        Exceptions: Index Error - if the coordinates are out of bounds
        '''
        # TODO: Body
        pass

    def shape(self):
        '''
        Returns a tuple containing the (x, y) size of the Battlefield

        Returns: Tuple containing the size of the Battlefield (non-negative int, non-negative int)
        '''
        # TODO: Body
        pass

    # TODO: More stuff

