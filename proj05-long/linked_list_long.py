"""
Name: Jacob Truman
file_name: linked_list_long.py
Purpose: multiple different functions that can be used in other files.
Can be used to determine if a linked list is sorted, the int value
of the nodes, breaking it apart, combining them together, or breaking
it apart in a strange manner
CSC 120 Fall 2021
"""
import list_node

def sorted_helper(head):
    """ 
    determines if the length of the linked list
    is long enough to need to iterate through it
    """
    length = 0
    curr = head
    while curr is not None:
        length += 1
        curr = curr.next
    return length

def is_sorted(head):
    """ 
    looks at the current pointer and the next pointer to determine
    if the values are in the correct order
    Parameters: head pointer
    Returns: boolean
    Pre-condition: head pointer
    Post-condition: True or False
    """
    length = sorted_helper(head)
    if length <= 1:
        return True
    curr = head
    while curr is not None and curr.next is not None:
        if curr.val > curr.next.val:
            return False
        curr = curr.next
    return True

def list_sum(head):
    """ 
    looks at the value of each node in the linked list
    then totals up all the values
    Parameters: linked list head pointer
    Returns: the value of the list node values
    Pre-condition: linked list head pointer
    Post-condition: integer
    """
    value = 0
    curr = head
    while curr is not None:
        value += curr.val
        curr = curr.next
    return value

def remove_helper(head):
    '''
    helps in partition list in making the end node correct
    '''
    curr = head
    while curr.next.next is not None:
        curr = curr.next
    curr.next = None
    return head

def partition_list(head):
    """ 
    Uses a linked list to create two new lists, storing 
    each node in either a list or b list
    Parameters: linked list head pointer
    Returns: alternate values of the original list in two seperate lists
    Pre-condition: a linked list
    Post-condition: two new linked lists
    """
    if head is None:
        return None, None
    if head.next is None:
        return head, None
    list1 = head
    tail1 = list1
    list2 = head.next
    tail2 = list2
    curr = head.next.next
    checker = True
    while curr is not None:
        if checker:
            tail1.next = curr
            checker = False
            tail1 = tail1.next
        else:
            tail2.next = curr
            checker = True
            tail2 = tail2.next
        curr = curr.next
    list2 = remove_helper(list2)
    return list1, list2

def accordion_4(head, start_pos):
    """ 
    Takes in a linked list and a starting posistion, then
    makes a new list while removing 3 of 4 nodes of the old list
    Parameters: linked list, starting posistion
    Returns: new linked list using the old list
    Pre-condition: linked list with a posistion starter
    Post-condition: am updated linked list
    """
    new_head = None
    curr = head
    place = 0
    while curr is not None:
        if place == start_pos:
            new_head = curr
            break
        place += 1
        curr = curr.next
    new_tail = new_head
    counter = 1
    while curr is not None:
        if counter == 5:
            new_tail.next = curr
            new_tail = new_tail.next
            counter = 1
        counter += 1
        curr = curr.next
        new_tail.next = None
    return new_head

def pair(list1, list2):
    """ 
    Takes in two linked lists in order to make
    tuples of their values, stored in a linked list
    Parameters: two linked lists
    Returns: tuple of the values of the two linked lists
    Pre-condition: Two linked lists
    Post-condition: one combined linked list
    """
    head = list_node.ListNode(None)
    tail = head
    curr1 = list1
    curr2 = list2
    while curr1 is not None and curr2 is not None:
        tail.next = list_node.ListNode((curr1.val,curr2.val))
        curr1 = curr1.next
        curr2 = curr2.next
        tail = tail.next
    return head.next