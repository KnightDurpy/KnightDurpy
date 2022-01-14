""" 
File: classes_prob2.py
Author: Jacob Truman
Purpose: generates a color object using RGB standard,
has the ability to print in multiple ways, set specific colors,
and bounds it in a certain range
Class: CSC 120, Fall 2021 
"""
class Color:
    def __init__(self, r,g,b):
        """ 
        takes in the RGB values and bounds them in a certain range
        Parameters: r, g ,b color values
        Returns: NA
        Pre-condition: NA
        Post-condition: pointers made
        """
        self.__r = self.bound(r)
        self.__g = self.bound(g)
        self.__b = self.bound(b)

    def bound(self,color):
        """ 
        makes sure the values are between 0 and 255
        Parameters: the color that is in question
        Returns: bound color value
        Pre-condition: unbound color
        Post-condition: bound color
        """
        if color < 0:
            color = 0
            return color
        if color > 255:
            color = 255
            return color
        return color

    def __str__(self):
        """ 
        using the color values, turns in into tuple like string
        Parameters: NA
        Returns: String
        Pre-condition: NA
        Post-condition: temp string
        """
        return 'rgb('+str(self.__r)+','+str(+self.__g)+','+str(self.__b)+')'

    def html_hex_color(self):
        """ 
        uses a formatting method to convert the RGB values
        into a string statement
        Parameters: NA
        Returns: string statement
        Pre-condition: NA
        Post-condition: String
        """
        return '#%02X%02X%02X' % (self.__r, self.__g, self.__b)

    def get_rgb(self):
        """ 
        makes and returns a tuple of the RGB values
        Parameters: NA
        Returns: tuple of RGB
        Pre-condition: NA
        Post-condition: return statement
        """
        return (self.__r,self.__g,self.__b)

    def set_standard_color(self, name):
        """ 
        gets a color name in and sets the color values 
        to the proper RGB values
        Parameters: color name
        Returns: NA
        Pre-condition: RGB values
        Post-condition: updated RGB values based on the color stadard
        """
        if name.lower() == 'red':
            self.__r = 255
            self.__g , self.__b = 0 , 0
        elif name.lower() == 'yellow':
            self.__r , self.__g = 255, 255
            self.__b = 0
        elif name.lower() == 'white':
            self.__r, self.__g, self.__b = 255, 255, 255
        elif name.lower() == 'black':
            self.__r, self.__b, self.__g = 0, 0, 0

    def remove_red(self):
        """ 
        removes all of the red color in the RGB value
        Parameters: NA
        Returns: NA
        Pre-condition: red value
        Post-condition: red value is now zero
        """
        self.__r = 0