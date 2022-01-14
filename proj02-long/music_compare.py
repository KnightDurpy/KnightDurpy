""" 
File: music_compare.py
Author: Jacob Truman
Purpose: this program runs in tandem with utils.py,
this program actually gives out the info that util.py
generates.
Class: CSC 120, Fall 2021 
"""

from utils import *

def song_list(file):
    """ 
    opens a song file and prints out all the information
        about the music and generates the lists that are
        needed for later
    Parameters: file with music information
    Returns: the first song information, all other songs information
        and the file to close
    Pre-condition: None
    Post-condition: return
    """
    print('--- SONG LIST ---')
    file_open = open(file, 'r')
    song_list = read_file(file_open)
    first_id = ()
    song_ids = []
    for x in song_list:
        if first_id == ():
            first_id = (str(x[0]), str(x[1]),x[2])
        song_ids.append((str(x[0]), str(x[1]), x[2]))
        print('id='+str(x[0])+' info="'+str(x[1])+'" notes='+str(x[2]))
    print()
    return first_id, song_ids, file_open

def cmd_comparisons(first_id, song_ids, num):
    """ 
    compares all the music using the rist song as a base
    Parameters: first song id, all other songs ids, and number
        for set comparison
    Returns: the best pair of songs
    Pre-condition: file opened
    Post-condition: returns a list 
    """
    print('--- COMPARISONS ---')
    best_pair = ()
    max = -1
    comparisons = []
    for id in song_ids:
        if id == first_id:
            continue
        comparison = compare_melodies(first_id[2],id[2],num)
        comparisons.append((id, comparison))
        if comparison > max:
            max = comparison
            best_pair = (id[0],id[1],id[2])
    for tup in sorted(comparisons):
        print(f'id_a={first_id[0]} id_b={tup[0][0]} similarity={tup[1]}')
    print()
    return best_pair

def results(first_id, best_pair):
    """ 
    prints out the best pair song information and id's
    Parameters: frst id and the best pair information
    Returns: None
    Pre-condition: NA
    Post-condition: Print statements
    """
    print('--- RESULT ---')
    print('Most similar songs:')
    print('  '+first_id[1])
    print('  '+best_pair[1])
    print()
    print('  ids: '+first_id[0])
    print('  ids: '+best_pair[0])
    print()

def melodies(first_id, best_pair):
    """ 
    prints out all the  notes that are in the two songs
    Parameters: first id and best pair information
    Returns: None
    Pre-condition: NA
    Post-condition: print statements
    """
    print('Melodies:')
    print('  ',end='')
    for note in first_id[2]:
        print(note,end=' ')
    print()
    print('  ',end='')
    for note in best_pair[2]:
        print(note,end=' ')
    print()
    print()

def cmd_set(first_id, best_pair, num):
    """ 
    prints out all possible sets of notes that first id
        and the best pair could have
    Parameters: first id, best pair, and the number for set length
    Returns: None
    Pre-condition: NA
    Post-condition: print statements
    """
    print('Set 1')
    hold = get_slices(first_id[2],num)
    all_poss = []
    for i in hold:
        if i in all_poss:
            continue
        all_poss.append(i)
    for item in sorted(all_poss):
        print(' ',end='')
        string = ''
        for e in item:
            string += ' '+e
        print(string)
    print()
    print('Set 2')
    hold = get_slices(best_pair[2],num)
    all_poss2 = []
    for i in hold:
        if i in all_poss2:
            continue
        all_poss2.append(i)
    for item in sorted(all_poss2):
        print(' ',end='')
        string = ''
        for e in item:
            string += ' '+e
        print(string)

def main():
    """ 
    takes an input to be sent to read_file, which then gives
    the song list, then comparisons of the songs are produced,
    finally several reseults are given about the music.
    Parameters: None
    Returns: a song list and info, their comparisons, and
    reports results of the information
    Pre-condition: Is called to run
    Post-condition: The return value is a number. 
    """

    file = input('file: ')
    num = int(input('n: '))

    first_id, song_ids, file_open = song_list(file)
    best_pair = cmd_comparisons(first_id, song_ids, num)
    results(first_id, best_pair)
    melodies(first_id, best_pair)
    cmd_set(first_id, best_pair, num)
    
    file_open.close()

main()