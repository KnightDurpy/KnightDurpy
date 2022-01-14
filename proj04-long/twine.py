"""
Name: Jacob Truman
file_name: twine.py
purpose: Takes user input for an obstacle file, then uses user input
to move the 'character' arround. They can also ask to see the map,
how many times they have been at their current posistion, and the range
of their movement.
CSC 120 Fall 2021
"""
# I read that deque be used, it is faster than using a list
# as stack but gives out a bad print
# from collections import deque

def obstacle_construction(prompt):
    """ 
    Using the file name, will try and locate the file to be used,
    which will be used to check if movement is allowed
    Parameters: File name
    Returns: obstacles list
    Pre-condition: File name given
    Post-condition: Makes the obstacles file
    """
    if prompt == '-':
        return
    else:
        file_open = open(prompt, 'r')
        file_lines = file_open.readlines()
        obstacles = []
        for line in file_lines:
            line = line.strip()
            line = line.split()
            if len(line) > 2 or (line[0].strip('-')).isnumeric() == False \
                            or (line[1].strip('-')).isnumeric() == False:
                print('ERROR: Line has something invalid')
                continue
            line = (int(line[0]), int(line[1]))
            obstacles.append(line)
        file_open.close()
    return obstacles

def move_allow(move_list, obstacles):
    """ 
    Looks at the most recent posistion and checks to see
    if the move is allowed an not in the obstacles file
    If the file doesn't exist it would throw an error but is handled
    Parameters: the move_list and obstacles
    Returns: updated move_list
    Pre-condition: move_list and obstacles are given
    Post-condition: returns updated move list
    """
    newest_move = move_list[-1]
    try:
        for obs in obstacles:
            if newest_move == obs:
                print('You could not move in that direction',end='')
                print(', because there is an obstacle in the way.')
                print('You stay where you are.')
                move_list.pop()
                # return move_list
                break
    except TypeError:
        return move_list
    return move_list

# move north cmd
def north_move(move_list, obstacles):
    """ 
    Using move_list, adds the move in and then checks if it
    is moving to an obstacle
    Parameters: the move_list and obstacles
    Returns: updated move_list
    Pre-condition: move_list and obstacles are given
    Post-condition: The return updated move list
    """
    new_move = (move_list[-1][0], move_list[-1][1]+1)
    move_list.append(new_move)
    move_list = move_allow(move_list, obstacles)
    return move_list
# move south cmd
def south_move(move_list, obstacles):
    """ 
    Using move_list, adds the move in and then checks if it
    is moving to an obstacle
    Parameters: the move_list and obstacles
    Returns: updated move_list
    Pre-condition: move_list and obstacles are given
    Post-condition: The return updated move list
    """
    new_move = (move_list[-1][0], move_list[-1][1]-1)
    move_list.append(new_move)
    move_list = move_allow(move_list, obstacles)
    return move_list
# move east cmd
def east_move(move_list, obstacles):
    """ 
    Using move_list, adds the move in and then checks if it
    is moving to an obstacle
    Parameters: the move_list and obstacles
    Returns: updated move_list
    Pre-condition: move_list and obstacles are given
    Post-condition: The return updated move list
    """
    new_move = (move_list[-1][0]+1, move_list[-1][1])
    move_list.append(new_move)
    move_list = move_allow(move_list, obstacles)
    return move_list
# move west cmd
def west_move(move_list, obstacles):
    """ 
    Using move_list, adds the move in and then checks if it
    is moving to an obstacle
    Parameters: the move_list and obstacles
    Returns: updated move_list
    Pre-condition: move_list and obstacles are given
    Post-condition: The return updated move list
    """
    new_move = (move_list[-1][0]-1, move_list[-1][1])
    move_list.append(new_move)
    move_list = move_allow(move_list, obstacles)
    return move_list
# back cmd
def back_move(move_list):
    """ 
    Uses the move list to remove the top of the stack
    Parameters: file is given with move information
    Returns: an updated move list
    Pre-condition: a file is given
    Post-condition: Move list shorter by one
    """
    if len(move_list) == 1:
        print("Cannot move back, as you're at the start!")
    else:
        move_list.pop()
        print('You retrace your steps by one space')
    return move_list

# crossing cmd
def check_crossings(move_list):
    """ 
    Uses move list to determine how many times the character
    has been at their current location
    Parameters: file is given with all current moves
    Returns: a print statement about the amount of times at a single place
    Pre-condition: a file is given
    Post-condition: Print statement
    """
    curr_pos = move_list[-1]
    cross_count = 0
    for move in move_list:
        if move == curr_pos:
            cross_count+=1
    print('There have been '+str(cross_count),end='')
    print(' times in the history when you were at this point.')

# ranges cmd
def check_ranges(move_list):
    """ 
    This will take in the list of moves, which will be searched
    in order to find the furthest it travels in any direction
    Parameters: List of moves is gievn
    Returns: print statements
    Pre-condition: list of moves
    Post-condition: Print statements
    """
    west_max = 0
    east_max = 0
    south_max = 0
    north_max = 0
    for move in move_list:
        if move[0] < 0 and move[0] < west_max:
            west_max = move[0]
        if move[0] > east_max:
            east_max = move[0]
        if move[1] < 0 and move[1] < south_max:
            south_max = move[1]
        if move[1] > north_max:
            north_max = move[1]
    print('The furthest West your twine goes is '+str(west_max))
    print('The furthest East your twine goes is '+str(east_max))
    print('The furthest South your twine goes is '+str(south_max))
    print('The furthest North your twine goes is '+str(north_max))

# map cmd
def make_map(move_list,obstacles):
    """ 
    Takes in the moves and obstacles, using this it will
    generate a llist of string which represents the map of the maze
    Parameters: List of all current moves, and obstacles present
    Returns: a print out of the map
    Pre-condition: Two files in
    Post-condition: No data changes
    """
    cap = '+-----------+'
    adj = 6
    # upside-down
    map = []
    print(cap)
    for y in range(-5,6):
        rows_of_columns = '|           |'
        list_roc = list(rows_of_columns)
        for move in move_list:
            if move == (0,0) and y == 0:
                list_roc[move[0]+adj] = '*'
                rows_of_columns = ''.join(list_roc)
                continue
            if move[1] == y:
                list_roc[move[0]+adj] = '.'
                rows_of_columns = ''.join(list_roc)
            if move[1] == y and move == move_list[-1]:
                list_roc[move[0]+adj] = '+'
                rows_of_columns = ''.join(list_roc)
        try:
            for obs in obstacles:
                if obs[1] == y:
                    list_roc[obs[0]+adj] = 'X'
                    rows_of_columns = ''.join(list_roc)
        except Exception:
            map.append(rows_of_columns)
            continue
        map.append(rows_of_columns)
    for row in reversed(map):
        print(row)
    print(cap)

def main():
    """ 
    Sets up the obstacle file, and does the main prints
    and input to use twine
    Parameters: None
    Returns: print statements
    Pre-condition: None
    Post-condition: multiple print statements
    """
    checker = True
    while checker:
        # this try except could be in the function
        try:
            print('Please give the name of the obstacles filename,',end='')
            print(' or - for none: ')
            prompt = input()
            if prompt == '':
                print('ERROR: no file name given and did not use "-"')
                print()
                continue
            obstacles = obstacle_construction(prompt)  # obstacles is a tuple
            checker = False
        except FileNotFoundError:
            print('ERROR: File not found')
    # print(obstacles)
    checker = True
    move_list = [(0,0)]  # stack of tuples
    while checker:
        print('Current position: '+str(move_list[-1]))
        print('Your history:     '+str(move_list))
        print('What is your next command?')
        try:
            action = input()
            action = action.split()
        except EOFError:
            break
        # determine action
        if len(action) > 1:
            print('ERROR: too many words in command, only one word allowed')
            print()
            continue
        if action == []:
            print('You do nothing.')
            print()
            continue
        action = action[0]
        if action == 'n':
            move_list=north_move(move_list,obstacles)
            print()
            continue
        if action == 's':
            move_list=south_move(move_list,obstacles)
            print()
            continue
        if action == 'e':
            move_list=east_move(move_list,obstacles)
            print()
            continue
        if action == 'w':
            move_list=west_move(move_list,obstacles)
            print()
            continue
        if action == 'back':
            move_list=back_move(move_list)
            print()
            continue
        if action == 'crossings':
            check_crossings(move_list)
            print()
            continue
        if action == 'map':
            make_map(move_list, obstacles)
            print()
            continue
        if action == 'ranges':
            check_ranges(move_list)
            print()
            continue
        print('ERROR: You have not given a proper command.')
        print()
        
    

if __name__ == '__main__':
    main()