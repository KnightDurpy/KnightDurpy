'''
File: linked_list_recursion_part2.py
Author: Jacob Truman
Purpose: has three different functions, one to convert an array to a
    linked list, another to remove nodes from a linked list and keep
    the pointers the same, and a third to pair the nodes from to 
    lists together.
Class: CSC 120, Fall 2021
'''
import list_node
def array_to_list_recursive(data):
    '''
    takes in an array and converts it into a linked list
    Parameters: array to be converted
    Pre-condition: an array
    post-condition: linked list
    '''
    if data == []:
        return None
    new_node = list_node.ListNode(data[0])
    new_node.next = array_to_list_recursive(data[1:])
    return new_node

def accordion_recursive(head):
    '''
    takes in a linked list and removes every other node
    starting with the first node
    Parameters: pointer of a linked list
    Pre-condition: a full linked list
    post-condition: a modified linked list
    '''
    if head is None:
        return None
    if head.next is None:
        return None
    curr = head.next
    curr.next = accordion_recursive(curr.next)
    return curr

def pair_recursive(head1, head2):
    '''
    takes in two node pointers and pairs them together
    stops if either list has finished
    Parameters: two linked list pointers
    Pre-condition: two linked lists
    post-condition: tuple of the original two lists pointers
    '''
    if head1 is None or head2 is None:
        return None
    new_node = list_node.ListNode((head1.val,head2.val))
    new_node.next = pair_recursive(head1.next, head2.next)
    return new_node