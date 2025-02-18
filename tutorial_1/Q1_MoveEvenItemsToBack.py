def moveEvenItemsToBack(ll):
    if ll.size < 2:
        return
    
    cur = ll.head
    index = 0
    for _ in range(ll.size):
        if cur.item % 2 == 0:
            even_value
