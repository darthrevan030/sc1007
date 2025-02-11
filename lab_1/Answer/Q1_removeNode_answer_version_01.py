class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

def printList(head):
    print("Current List:", end=" ")
    cur = head
    while cur is not None:
        print(cur.item, end=" ")
        cur = cur.next
    print()

def findNode(head, index):
    if head is None or index < 0:
        return None
    cur = head
    while index > 0:
        cur = cur.next
        if cur is None:
            return None
        index -= 1
    return cur

def insertNode(ptrHead, index, value):
    newNode = ListNode(value)
    if ptrHead is None:
        return newNode
    if index == 0:
        newNode.next = ptrHead
        return newNode
    cur = ptrHead
    prev = None
    count = 0
    while cur is not None and count < index:
        prev = cur
        cur = cur.next
        count += 1
    if prev is not None:
        prev.next = newNode
        newNode.next = cur
    return ptrHead

################################################################################################################################
def removeNode(ptrHead, index):
    # Check if there is only one node in the list, if not, remove the first node
    if ptrHead.next is not None:
        ptrHead.item = ptrHead.next.item
        temp = ptrHead.next
        ptrHead.next = ptrHead.next.next
        del temp
    # If there is only one node in the list, remove it and set the head to None
    else:
        ptrHead = None
    return 1
##############################################################################################################################

if __name__ == "__main__":
    head = None
    size = 0
    print("Enter one number per line (press Enter after each number).")
    print("Enter any non-digit character to finish input:")
    while True:
        try:
            item = int(input())
            head = insertNode(head, size, item)
            size += 1
        except ValueError:
            break
    printList(head)
    
    while True:
        try:
            index = int(input("Enter the index of the node to be removed: "))
            result = removeNode(head, index)
            if result == 1:
                size -= 1
                print("Node successfully removed")
            else:
                print("Removal failed")
            print("After the removal operation:")
            printList(head)
        except ValueError:
            break
    printList(head)