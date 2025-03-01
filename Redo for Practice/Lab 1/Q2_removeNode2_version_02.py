class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert2(self, item, index):
        new_node = ListNode(item)

        # Handle insertion at beginning
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True
    
        # Find node before insertion point
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1
    
        # Check if position is valid
        if not current:
            print("Index out of range")
            return False
        
        # Insert the new node
        new_node.next = current.next
        current.next = new_node
        self.size += 1
        return True
    
    def printList2(self):
        if self.head is not None:
            cur = self.head
            print(f"Current List has {self.size} elements: ", end="")
            while cur is not None:
                print(cur.item, end=" ")
                cur = cur.next
            print()

#################################################################################################################################################
    def remove2(self, index):
        if self.head is None:
            print("List is empty")
            return 0
        
        if index == 0:
            if self.head is not None:
                cur = self.head
                self.head = cur.next
                del cur
                self.size -= 1
                return 1
            
        cur = self.head
        count = 0
        while cur and count < index - 1:
            cur = cur.next
            count += 1
        
        if not cur or not cur.next:
            print("Index out of range")
            return 0
        
        temp = cur.next
        cur.next = temp.next
        del temp
        self.size -= 1 
        
        return 1
#################################################################################################################################################

if __name__ == "__main__":
    ll = LinkedList()
    print("Enter one number per line (press Enter after each number).")
    print("Enter any non-digit character to finish input:")
    try:
        while True:
            item = int(input())
            if not ll.insert2(item, ll.size):
                break
    except ValueError:
        pass
    ll.printList2()
    
    while True:
        try:
            index = int(input("Enter the index of the node to be removed: "))
            if not ll.remove2(index):
                print("The node cannot be removed.")
                break
            print("After the removal operation:")
            ll.printList2()
        except ValueError:
            break
    ll.printList2()