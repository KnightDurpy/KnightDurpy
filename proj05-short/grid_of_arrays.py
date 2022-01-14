import list_node

def grid_of_arrays():
    three_three = [None,(2,2),None]
    two_three = [three_three,(1,2),None]
    one_three = [two_three,(0,2),None]
    three_two = [None,(2,1),three_three]
    two_two = [three_two,(1,1),two_three]
    one_two = [two_two,(0,1),one_three]
    three_one = [None,(2,0),three_two]
    two_one = [three_one,(1,0),two_two]
    one_one = [two_one,(0,0),one_two]
    return one_one