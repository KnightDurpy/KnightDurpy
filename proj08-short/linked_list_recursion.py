def is_sorted_recursive(head):
    if head == None or head.next == None:
        return True
    if head.next.val >= head.val:
        return is_sorted_recursive(head.next)
    return False

def is_sorted(head):
    if head is None:
        return True
    if head.next is None:
        return True
    curr = head
    hold = None
    while curr is not None:
        if hold is None:
            hold = curr.val
            curr = curr.next
            continue
        if curr.val < hold:
            return False
        hold = curr.val
        curr = curr.next
    return True