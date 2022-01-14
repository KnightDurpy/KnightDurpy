""" 
File: utils.py
Author: Jacob Truman
Purpose: This program turns an input into a tuple,
slice the notes, and do two comparisons
Class: CSC 120, Fall 2021 
"""

def read_file(file):
    """ 
    takes the file data and turns it into three seperate
    lists, then turns those into a tuple.
    Parameters: file is given with music information
    Returns: a tuple
    Pre-condition: a file is given
    Post-condition: The return is a tuple 
    """
    list_num = []
    list_names = []
    list_melody = []
    file_lines = file.readlines()
    for line in file_lines:
        new_line = line.strip('\n')
        if new_line == '':
            continue
        if line[0] == '@':
            list_names.append(new_line[6:])
            list_num.append(int(new_line[2:5].lstrip('0')))
        else:
            list_melody.append(new_line.split(' '))
    if '' in list_melody:
        list_melody.remove('')
    return list(zip(list_num, list_names, list_melody))

def get_slices(data, length):
    """ 
    takes the music notes given and slices them into
    each possible unique sets.
    Parameters: music note data and the length wanted
    Returns: a list of notes
    Pre-condition: data is a list, and Length is a number
    Post-condition: slices are returned 
    """
    result = []
    for x in range(len(data)-length+1):
        result.append(data[x : x + length])
    return result

def compare_sets(info_1, info_2):
    """ 
    Two lists are used to compare their
    simularities and returns a number from
    0.0 to 1.0.
    Parameters: two sets
    Returns: a Jaccard index
    Pre-condition: two lists are given
    Post-condition: returns a Jaccard index 
    """

    if info_1 == set() and info_2 == set():
        return 1
    else:
        set_1 = set(info_1)
        set_2 = set(info_2)
        return float(len(set_1.intersection(set_2)) / len(set_1.union(set_2)))

def compare_melodies(melody_1, melody_2, num):
    """ 
    Takes to melody pieces and transforms them in a way
    that allows for a Jaccard index to be produced.
    Parameters: two melody pieces and a comparison
    number.
    Returns: A number that is between 0.0 and 1.0
    Pre-condition: two slices of notes
    Post-condition: a Jaccard index is returned
    """
    
    slice_1 = get_slices(melody_1, num)
    slice_2 = get_slices(melody_2, num)
    slice_1_set = set()
    slice_2_set = set()
    for slice_first in slice_1:
        tuple_first = tuple(slice_first)
        slice_1_set.add(tuple_first)
    for slice_second in slice_2:
        tuple_second = tuple(slice_second)
        slice_2_set.add(tuple_second)
    comparison = compare_sets(slice_1_set, slice_2_set)
    return comparison