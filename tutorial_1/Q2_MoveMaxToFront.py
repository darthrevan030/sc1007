def moveMaxToFront(ll):
    if ll.head is None or ll.head.next is None:
        return -1

    pre_max = None
    max_node = ll.head #Assume 1st node is biggest
    cur = ll.head

    while cur.next is not None: #Check terminating condition
        if cur.next.item > max_node.item: #if find a node bigger than current max
            pre_max = cur #adjust pointer to the new biggest
            max_node = cur.next
        cur = cur.next

    if pre_max is None: #Max is alr at the front
        return 0
    #move the max node to the front
    pre_max.next = max_node.next
    max_node.next = ll.head
    ll.head = max_node

    return 0
