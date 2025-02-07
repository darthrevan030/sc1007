def remove_duplicates_sorted(ll):
    current = ll.head
    if current is None:
        return
    
    while current.next is not None:
        if current.item == current.next.item:
            temp = current.next.next
            current.next = temp
            ll.size -= 1
        else:
            current = current.next
            