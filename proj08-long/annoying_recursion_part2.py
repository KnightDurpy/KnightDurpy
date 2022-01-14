'''
File: annoying_recursion_part2.py
Author: Jacob Truman
Purpose: this program has three different functions,
    one that takes a number and adds that to all numbers that come before it
    another that makes a list of fibonacci numbers to the nth place
    and another that prints out a valley like image with n height
Class: CSC 120, Fall 2021
'''
def annoying_triangleNumbers(n):
    '''
    takes in an n integer and adds that to all integers before it
    Parameters: n integer
    Pre-condition: None
    post-condition: triangle number
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n == 3:
        return 6
    if n == 4:
        return 4 + annoying_triangleNumbers(3)
    if n == 5:
        return 5 + annoying_triangleNumbers(4)
    if n == 6:
        return 6 + annoying_triangleNumbers(5)
    return n + annoying_triangleNumbers(n-1)

def annoying_fibonacci_sequence(n):
    '''
    takes in an n interger which used to determine
        the length of the array
    Parameters: n size
    Pre-condition: None
    post-condition: fibonacci array
    '''
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0,1]
    if n == 3:
        return [0,1,1]
    if n == 4:
        return annoying_fibonacci_sequence(3)+[2]
    if n == 5:
        return annoying_fibonacci_sequence(4)+[3]
    if n == 6:
        return annoying_fibonacci_sequence(5)+[5]
    return annoying_fibonacci_sequence(n-1) + annoying_fibonacci_sequence(n-2)

def annoying_valley(n):
    '''
    takes in a n value and uses that to print out a valley like shape
    Parameters: n size of valley
    Pre-condition: None
    post-condition: a printed valley shape
    '''
    if n == 0:
        print()
    elif n == 1:
        print('*')
    elif n == 2:
        print('./')
        print('*')
        print('.\\')
    elif n == 3:
        print('../')
        print('./')
        print('*')
        print('.\\')
        print('..\\')
    elif n == 4:
        print('.'*3+'/')
        annoying_valley(3)
        print('.'*3+'\\')
    elif n == 5:
        print('.'*4+'/')
        annoying_valley(4)
        print('.'*4+'\\')
    elif n == 6:
        print('.'*5+'/')
        annoying_valley(5)
        print('.'*5+'\\')
    else:
        print('.'*(n-1)+'/')
        annoying_valley(n-1)
        print('.'*(n-1)+'\\')