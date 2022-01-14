""" 
File: classes_prob1.py
Author: Jacob Truman
Purpose: multiple different class objects
Class: CSC 120, Fall 2021 
"""
class Simplest:
    def __init__(self, a, b, c):
        """ 
        holds three objects in a class
        Parameters: a, b, c inputs
        Returns: NA
        Pre-condition: NA
        Post-condition: a, b, c objects
        """
        self.a = a
        self.b = b
        self.c = c

class Rotate:
    def __init__(self,first,second,third):
        """ 
        makes a first, second, and third objects
        Parameters: first, second, third
        Returns: NA
        Pre-condition: NA
        Post-condition: 3 self objects
        """
        self.__first = first
        self.__second = second
        self.__third = third
    def get_first(self):
        """ 
        return the first pointer
        Parameters: NA
        Returns: first pointer
        Pre-condition: NA
        Post-condition: returns first
        """
        return self.__first
    def get_second(self):
        """ 
        returns the second pointer
        Parameters: NA
        Returns: second pointer
        Pre-condition: NA
        Post-condition: returns second
        """
        return self.__second
    def get_third(self):
        """ 
        returns the third pointer
        Parameters: NA
        Returns: the third pointer
        Pre-condition: NA
        Post-condition: returns third
        """
        return self.__third
    def rotate(self):
        """ 
        takes the 3 pointers and roates their posistions, essentially
        moves first to third, second to first, third to second
        Parameters: NA
        Returns: NA
        Pre-condition: NA
        Post-condition: rotated posistions
        """
        hold_first = self.__first
        hold_second = self.__second
        hold_third = self.__third
        self.__first = hold_second
        self.__second = hold_third
        self.__third = hold_first

class Band:
    def __init__(self,singer):
        """ 
        creates singers, a drummer, and a list of guitar players
        Parameters: a singer name
        Returns: NA
        Pre-condition: NA
        Post-condition: singer, drummer, and guitar players arranged
        """
        self.__singer = singer
        self.__drummer = None
        self.__guitar = []
    def get_singer(self):
        """ 
        returns the singers name
        Parameters: NA
        Returns: singers name
        Pre-condition: NA
        Post-condition: returns singer
        """
        return self.__singer
    def set_singer(self, new_singer):
        """ 
        updates the singers name to something else
        Parameters: new singers name
        Returns: NA
        Pre-condition: old singer
        Post-condition: new singer is made
        """
        self.__singer = new_singer
    def get_drummer(self):
        """ 
        returns the drummers name
        Parameters: NA
        Returns: drummer name
        Pre-condition: NA
        Post-condition: returns drummer
        """
        return self.__drummer
    def set_drummer(self, new_drummer):
        """ 
        updates the drummers name to something else
        Parameters: new drummer name
        Returns: NA
        Pre-condition: old drummer
        Post-condition: new drummer is made
        """
        self.__drummer = new_drummer
    def fire_all_guitar_players(self):
        """ 
        removes all current guitar players
        Parameters: NA
        Returns: NA
        Pre-condition: list of guitar players
        Post-condition: empty list
        """
        self.__guitar = []
    def add_guitar_player(self, new_guitar_player):
        """ 
        puts a new guitar player into the band
        Parameters: new guitar player name
        Returns: NA
        Pre-condition: list of guitar players
        Post-condition: updated guitar list
        """
        self.__guitar.append(new_guitar_player)
    def get_guitar_players(self):
        """ 
        returns a copied list of guitar players
        Parameters: NA
        Returns: list of guitar players
        Pre-condition: NA
        Post-condition: coped list of guitar players
        """
        hold_guitar = []
        for player in self.__guitar:
            hold_guitar.append(player)
        return hold_guitar
    def play_music(self):
        """ 
        prints out music based on the players in the band
        Parameters: NA
        Returns: print statements
        Pre-condition: NA
        Post-condition: prints are made
        """
        if self.__singer == 'Frank Sinatra':
            print('Do be do be do')
        elif self.__singer == 'Kurt Cobain':
            print('bargle nawdle zouss')
        else:
            print('La la la')
        if self.__drummer is not None:
            print('Bang bang bang!')
        for i in self.__guitar:
            print('Strum!')