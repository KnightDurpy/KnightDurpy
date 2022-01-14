'''
File: Long_3.py
Author: Jacob Truman
Purpose: This program creates an animated graphic,
    it can also be modified with colors to change its look
Class: CSC 120, Fall 2021
'''
import graphics
from math import *

def center_cross(win, angle, angle2,color):
    '''
    Takes in win, two angles, and a color
    This will generate the center generated cross
    Parameters: window, two angles, and a color
    Pre-condition: multiple objects are given
    post-condition: a center cross is generated on the canvas
    '''
    win.line(200*cos(angle)+400,200*sin(angle)+400,-200*cos(angle)+400,-200*sin(angle)+400,color)
    win.line(200*cos(angle2)+400,200*sin(angle2)+400,-200*cos(angle2)+400,-200*sin(angle2)+400,color)

def middle_cross(win,angle,angle2,color):
    '''
    Takes in win, two angles, and a color
    This will generate 4 crosses and the end of the previous cross
    Parameters: window, two angles, and a color
    Pre-condition: multiple objects are given
    post-condition: 4 crosses are made on the canvas
    '''
    # probably could have been done better using a better method
    # right
    win.line(200*cos(angle)+400,200*sin(angle)+300,200*cos(angle)+400,200*sin(angle)+400,color)
    win.line(200*cos(angle)+400,200*sin(angle)+500,200*cos(angle)+400,200*sin(angle)+400,color)
    win.line(200*cos(angle)+300,200*sin(angle)+400,200*cos(angle)+400,200*sin(angle)+400,color)
    win.line(200*cos(angle)+500,200*sin(angle)+400,200*cos(angle)+400,200*sin(angle)+400,color)
        
    # left
    win.line(-200*cos(angle)+400,-200*sin(angle)+300,-200*cos(angle)+400,-200*sin(angle)+400,color)
    win.line(-200*cos(angle)+400,-200*sin(angle)+500,-200*cos(angle)+400,-200*sin(angle)+400,color)
    win.line(-200*cos(angle)+300,-200*sin(angle)+400,-200*cos(angle)+400,-200*sin(angle)+400,color)
    win.line(-200*cos(angle)+500,-200*sin(angle)+400,-200*cos(angle)+400,-200*sin(angle)+400,color)

    # top
    win.line(200*cos(angle2)+400,200*sin(angle2)+300,200*cos(angle2)+400,200*sin(angle2)+400,color)
    win.line(200*cos(angle2)+400,200*sin(angle2)+500,200*cos(angle2)+400,200*sin(angle2)+400,color)
    win.line(200*cos(angle2)+300,200*sin(angle2)+400,200*cos(angle2)+400,200*sin(angle2)+400,color)
    win.line(200*cos(angle2)+500,200*sin(angle2)+400,200*cos(angle2)+400,200*sin(angle2)+400,color)

    # bot
    win.line(-200*cos(angle2)+400,-200*sin(angle2)+300,-200*cos(angle2)+400,-200*sin(angle2)+400,color)
    win.line(-200*cos(angle2)+400,-200*sin(angle2)+500,-200*cos(angle2)+400,-200*sin(angle2)+400,color)
    win.line(-200*cos(angle2)+300,-200*sin(angle2)+400,-200*cos(angle2)+400,-200*sin(angle2)+400,color)
    win.line(-200*cos(angle2)+500,-200*sin(angle2)+400,-200*cos(angle2)+400,-200*sin(angle2)+400,color)

def outer_cross_1(win,angle,angle2,color):
    '''
    Takes in win, two angles, and a color
    This will generate a square at the end of one of the cross ends
    Parameters: window, two angles, and a color
    Pre-condition: multiple objects are given
    post-condition: 4 crosses are made on the canvas
    '''
    win.line(200*cos(angle)+450,200*sin(angle)+350,200*cos(angle)+400,200*sin(angle)+300,color)
    win.line(200*cos(angle)+350,200*sin(angle)+350,200*cos(angle)+400,200*sin(angle)+300,color)

    win.line(200*cos(angle)+450,200*sin(angle)+450,200*cos(angle)+400,200*sin(angle)+500,color)
    win.line(200*cos(angle)+350,200*sin(angle)+450,200*cos(angle)+400,200*sin(angle)+500,color)

    win.line(200*cos(angle)+300,200*sin(angle)+400,200*cos(angle)+350,200*sin(angle)+350,color)
    win.line(200*cos(angle)+300,200*sin(angle)+400,200*cos(angle)+350,200*sin(angle)+450,color)

    win.line(200*cos(angle)+500,200*sin(angle)+400,200*cos(angle)+450,200*sin(angle)+350,color)
    win.line(200*cos(angle)+500,200*sin(angle)+400,200*cos(angle)+450,200*sin(angle)+450,color)

def outer_cross_2(win,angle,angle2,color):
    '''
    Takes in win, two angles, and a color
    This will generate a square at the end of one of the cross ends
    Parameters: window, two angles, and a color
    Pre-condition: multiple objects are given
    post-condition: 4 crosses are made on the canvas
    '''
    win.line(-200*cos(angle)+400,-200*sin(angle)+300,-200*cos(angle)+500,-200*sin(angle)+400,color)
    win.line(-200*cos(angle)+400,-200*sin(angle)+300,-200*cos(angle)+300,-200*sin(angle)+400,color)

    win.line(-200*cos(angle)+400,-200*sin(angle)+500,-200*cos(angle)+500,-200*sin(angle)+400,color)
    win.line(-200*cos(angle)+400,-200*sin(angle)+500,-200*cos(angle)+300,-200*sin(angle)+400,color)

def outer_cross_3(win,angle,angle2,color):
    '''
    Takes in win, two angles, and a color
    This will generate a square at the end of one of the cross ends
    Parameters: window, two angles, and a color
    Pre-condition: multiple objects are given
    post-condition: 4 crosses are made on the canvas
    '''
    win.line(200*cos(angle2)+400,200*sin(angle2)+300,200*cos(angle2)+500,200*sin(angle2)+400,color)
    win.line(200*cos(angle2)+400,200*sin(angle2)+300,200*cos(angle2)+300,200*sin(angle2)+400,color)

    win.line(200*cos(angle2)+400,200*sin(angle2)+500,200*cos(angle2)+500,200*sin(angle2)+400,color)
    win.line(200*cos(angle2)+400,200*sin(angle2)+500,200*cos(angle2)+300,200*sin(angle2)+400,color)

def outer_cross_4(win,angle,angle2,color):
    '''
    Takes in win, two angles, and a color
    This will generate a square at the end of one of the cross ends
    Parameters: window, two angles, and a color
    Pre-condition: multiple objects are given
    post-condition: 4 crosses are made on the canvas
    '''
    win.line(-200*cos(angle2)+400,-200*sin(angle2)+300,-200*cos(angle2)+500,-200*sin(angle2)+400,color)
    win.line(-200*cos(angle2)+400,-200*sin(angle2)+300,-200*cos(angle2)+300,-200*sin(angle2)+400,color)

    win.line(-200*cos(angle2)+400,-200*sin(angle2)+500,-200*cos(angle2)+500,-200*sin(angle2)+400,color)
    win.line(-200*cos(angle2)+400,-200*sin(angle2)+500,-200*cos(angle2)+300,-200*sin(angle2)+400,color)
    
def main():
    '''
    This generates the main canvas, and sends information
        for the rest of the shapes
    Parameters: None
    Pre-condition: None
    post-condition: The entire canvas and objects are made
    '''
    print('Please give me seven colors')
    color1 = input('color 1: ')
    color2 = input('color 2: ')
    color3 = input('color 3: ')
    color4 = input('color 4: ')
    color5 = input('color 5: ')
    color6 = input('color 6: ')
    color7 = input('color 7: ')
    win = graphics.graphics(800,800, 'Animated 3')
    angle = 0
    angle2 = 55

    win.text()

    while not win.is_destroyed():
        win.rectangle(0,0,800,800,color1)
        angle+=.01
        angle2+=.01

        if angle > 360:
            angle = 0
            angle2 = 55
        
        win.clear()
        center_cross(win,angle,angle2,color2)
        middle_cross(win,angle,angle2,color3)
        outer_cross_1(win,angle,angle2,color4)
        outer_cross_2(win,angle,angle2,color5)
        outer_cross_3(win,angle,angle2,color6)
        outer_cross_4(win,angle,angle2,color7)
        
        win.update_frame(144)

if __name__ == '__main__':
    main()