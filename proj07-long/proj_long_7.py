'''
File: Long_7.py
Author: Jacob Truman
Purpose: This program creates an animated graphic,
    it can also be modified with colors to change its look
Class: CSC 120, Fall 2021
'''
from graphics import graphics
import three_shapes_game
import random

class Square:
    '''
    generates a square object in a random location
    on the board, it attempts to move to the center of the 
    canvas
    '''
    def __init__(self):
        self._x = random.randint(0,400)
        self._y = random.randint(0,400)
        self._rad = 25
        self._mover_x = 0
        self._mover_y = 0
        self._x_curr = self._x + self._mover_x
        self._y_curr = self._y + self._mover_y

    def get_xy(self):
        return ( self._x_curr , self._y_curr )

    def get_radius(self):
        return self._rad

    def nearby(self, other, dist, game):
        return

    def edge(self, dir, position):
        return

    def move(self, game):
        self._x_curr = self._mover_x + self._x
        if self._x_curr > 190:
            self._mover_x -= 1
        if self._x_curr < 190:
            self._mover_x += 1
        self._y_curr = self._mover_y + self._y
        if self._y_curr > 190:
            self._mover_y -= 1
        if self._y_curr < 190:
            self._mover_y += 1
        
    def draw(self, win):
        win.rectangle(self._x+self._mover_x,self._y+self._mover_y,self._rad,self._rad,'blue')

class Text:
    '''
    when the game ends, will display text saying
    that the game has ended
    '''
    def __init__(self):
        self._x = 100
        self._y = 150
    
    def draw(self, win):
        win.text(self._x,self._y,'Game Over!','black',24)

class Circle:
    '''
    makes the center black hole that determines if the
    game will end when it gets big enough
    '''
    def __init__(self):
        self._angle = 55
        self._x = 200
        self._y = 200
        self._rad = 25

    def get_xy(self):
        return ( self._x , self._y )

    def increase_radius(self):
        self._rad += 1

    def get_radius(self):
        return self._rad

    def nearby(self, other, dist, game):
        return 

    def edge(self, dir, position):
        return 

    def move(self, game):
        if self._angle > 365:
            self._angle = 0
        self._angle += 10

    def draw(self, win):
        win.ellipse(self._x,self._y,self._rad,self._rad,'black')

def spawn_more(game):
    '''
    makes anywhere from 1 to 0 objects when called
    Parameters: game object
    Pre-condition: None
    post-condition: generates more square objects
    '''
    amount = random.randint(0,1)
    for x in range(amount):
        new_object = Square()
        game.add_obj(new_object)

def remove_check(game, circle):
    '''
    looks to see if any objects have reached the center and will remove them if so
    Parameters: game and circle objects
    Pre-condition: large set of objects
    post-condition: objects in the center are removed
    '''
    active_objects = game.get_active_objects()
    for o in active_objects:
        if o.get_xy() == (190,190):
            game.remove_obj(o)
            circle.increase_radius()

def end_game_check(game, circle):
    '''
    if the circle has gotten big enough the game ends
    Parameters: game and circle object
    Pre-condition: game is on
    post-condition: game is over
    '''
    if circle.get_radius() > 400:
        game.set_game_over()
        true_all = game.get_active_objects()
        for o in true_all:
            game.remove_obj(o)


def main():
    '''
    Main logic of the program, runs the loops that create the
    canvas and adding of objects
    Parameters: None
    Pre-condition: NA
    post-condition: NA
    '''
    wid = 400
    hei = 400
    circle = Circle()
    game = three_shapes_game.Game('Black Hole', 20,wid, hei)
    game.add_obj(circle)
    while not game.is_over():
        game.do_move_calls()
        game.draw()
        spawn_more(game)
        remove_check(game, circle)
        end_game_check(game, circle)

    print('Game Over!')
    help = Text()
    game.add_obj(help)
    while game.is_over():
        game.draw()

if __name__ == "__main__":
    main()