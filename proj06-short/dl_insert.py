import dlist_node

def dl_insert_before(head, node, new_node):
    curr = head
    while curr is not None:
        if curr.val == node.val:
            if curr.val == head.val:
                new_node.next = head
                head.prev = new_node
                head = new_node
                break
            new_node.next = curr
            new_node.prev = curr.prev
            if curr.prev is not None:
                curr.prev.next = new_node
            curr.prev = new_node
        curr = curr.next
    return head

def dl_insert_after(head, node, new_node):
    curr = head
    while curr is not None:
        if curr.val == node.val:
            new_node.prev = curr
            new_node.next = curr.next
            if curr.next is not None:
                curr.next.prev = new_node
            curr.next = new_node
        curr = curr.next
    return head