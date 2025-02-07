class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

def printList(ll):
    cur = ll.head
    if cur is None:
        print("Empty")
        return
    while cur is not None:
        print(cur.item, end=" ")
        cur = cur.next
    print()

def findNode(ll, index):
    if ll is None or index < 0 or index >= ll.size:
        return None

    temp = ll.head
    while index > 0:
        temp = temp.next
        if temp is None:
            return None
        index -= 1

    return temp

def insertNode(ll, index, value):
    if ll is None or index < 0 or index > ll.size:
        return -1

    new_node = ListNode(value)

    if index == 0:  # Insert at the beginning
        new_node.next = ll.head
        ll.head = new_node
    else:
        pre = findNode(ll, index - 1)
        if pre is None:
            return -1
        new_node.next = pre.next
        pre.next = new_node

    ll.size += 1
    return 0

def removeNode(ll, index):
    if ll is None or index < 0 or index >= ll.size:
        return -1

    if index == 0:  # Remove the first node
        ll.head = ll.head.next
    else:
        pre = findNode(ll, index - 1)
        if pre is None or pre.next is None:
            return -1
        pre.next = pre.next.next

    ll.size -= 1
    return 0

def removeAllItems(ll):
    ll.head = None
    ll.size = 0

def moveMaxToFront(ll):
    if ll.head is None or ll.head.next is None:  # Empty list or single node
        return -1

    pre_max = None
    max_node = ll.head
    cur = ll.head

    while cur.next is not None:
        if cur.next.item > max_node.item:
            pre_max = cur
            max_node = cur.next
        cur = cur.next

    if pre_max is None:  # Max node is already at the front
        return 0

    # Move the max node to the front
    pre_max.next = max_node.next
    max_node.next = ll.head
    ll.head = max_node

    return 0

if __name__ == "__main__":
    ll = LinkedList()

    while True:
        print("1: Insert an integer to the linked list:")
        print("2: Move the largest stored value to the front of the list:")
        print("0: Quit:")

        choice = int(input("Please input your choice (1/2/0): "))

        if choice == 1:
            value = int(input("Input an integer that you want to add to the linked list: "))
            insertNode(ll, ll.size, value)
            print("The resulting linked list is:")
            printList(ll)
        elif choice == 2:
            moveMaxToFront(ll)
            print("The resulting linked list after moving the largest stored value to the front of the list is:")
            printList(ll)
        elif choice == 0:
            removeAllItems(ll)
            break
        else:
            print("Choice unknown.")
