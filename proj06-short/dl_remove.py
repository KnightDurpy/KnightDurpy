import dlist_node

def dl_remove(head,node_remove):
    if head is None or node_remove is None:
        return
    if head.next is None:
        if head.val == node_remove.val:
            new_head = None
        return new_head
    if head.val == node_remove.val:
        new_head = head.next
        new_head.prev = None
        return new_head
    curr = head
    while curr.next is not None:
        if curr.val == node_remove.val:
            break
        curr = curr.next
    if curr.next is not None:
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
    else:
        if curr.val == node_remove.val:
            curr.prev.next = None
    return head