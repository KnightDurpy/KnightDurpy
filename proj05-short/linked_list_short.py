import list_node

def list_to_array(head):
    new_array = []
    curr = head
    while curr is not None:
        new_array.append(curr.val)
        curr = curr.next
    return new_array

def array_to_list(data):
    head = None
    length = len(data)
    for i in range(0,length):
        hold = list_node.ListNode(data[i])
        if head is None:
            head = hold
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = hold
    return head

def list_length(head):
    length = 0
    curr = head
    while curr is not None:
        length += 1
        curr = curr.next
    return length

def split_list(head):
    length = 0
    curr = head
    while curr is not None:
        length+=1
        curr = curr.next
    
    if length < 2:
        head1 = head
        head2 = None
        return head1, head2
    curr = head
    half = (length-1) // 2
    for i in range(half):
        curr = curr.next
    head1 = head
    head2 = curr.next
    curr.next = None
    return head1, head2