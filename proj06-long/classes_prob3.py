""" 
File: classes_prob3.py
Author: Jacob Truman
Purpose: this generates a room object with directional pointers
much like doubly linked list
Class: CSC 120, Fall 2021 
"""
class Room:
    def __init__(self, x=0, y=0):
        """ 
        makes an object that has pointers North, South, East, West
        Parameters: x and y co-ordinates
        Returns: NA
        Pre-condition: None object
        Post-condition: pointers made
        """
        self.name = str((x,y))
        self.n = None
        self.s = None
        self.w = None
        self.e = None
        self.x = x
        self.y = y

    def get_name(self):
        """ 
        returns the name of the room
        Parameters: None
        Returns: name of the room
        Pre-condition: NA
        Post-condition: name returned
        """
        return self.name
    def set_name(self, new_name):
        """ 
        updates the objects name to something else
        Parameters: new_name
        Returns: NA
        Pre-condition: NA
        Post-condition: new name is made
        """
        self.name = new_name
    def collapse_room(self):
        """ 
        removes all directional pointers
        Parameters: NA
        Returns: NA
        Pre-condition: pointers to other rooms
        Post-condition: None pointers everywhere
        """
        self.n = None
        self.s = None
        self.w = None
        self.e = None

def build_grid_helper(i, j, curr, wid, hei):
    """ 
    generates a doubly linked 2D array
    Parameters: x and y posistion, current node, and limiters
    Returns: the head room pointer
    Pre-condition: NA
    Post-condition: new room objects pointing to each other
    """
    if i > wid or j > hei:
        return None
    new_room = Room(i,j)
    new_room.w = curr
    new_room.s = curr
    new_room.e = build_grid_helper(i,j+1,new_room,wid,hei)
    new_room.n = build_grid_helper(i+1,j,new_room,wid,hei)
    return new_room

def build_grid(wid,hei):
    """ 
    send information to helper function
    Parameters: width and height limits
    Returns: the southwest room
    Pre-condition: NA
    Post-condition: 2D matrix
    """
    return build_grid_helper(0,0,None, wid, hei)