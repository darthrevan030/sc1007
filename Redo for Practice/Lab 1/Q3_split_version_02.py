class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, index):
        new_node = Node(data)

        if self.head is None or index == 0:
            new_node.next = self.head
            self.head = new_node
            return True
    
        current = self.head
        count = 0
    
        while current and count < index - 1:
            current = current.next
            count += 1
    
        if not current:
            print("Index out of range")
            return False
        
        new_node.next = current.next
        current.next = new_node
        return True

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def deleteList(self):
        current = self.head
        while current:
            temp = current.next
            current.next = None
            current = temp
        self.head = None

#################################################################################################################################################
    def split(self):
        
        even_list = LinkedList()
        odd_list = LinkedList()

        if self.head is None:
            return even_list, odd_list
        
        cur = self.head

        while cur:
            if cur.data % 2 == 0:
                even_list.insert(cur.data, 0)
            else:
                odd_list.insert(cur.data, 0)
            cur = cur.next


        return even_list, odd_list
#################################################################################################################################################

if __name__ == "__main__":
    # Create main linked list
    linked_list = LinkedList()
    
    print("Enter one number per line (press Enter after each number).")
    print("Enter any non-digit character to finish input:")
    try:
        while True:
            item = int(input())
            if linked_list.insert(item, 0):  
                print(f"Successfully inserted {item}")
            else:
                print(f"Failed to insert {item}")
    except ValueError:
        pass

    print("\nBefore split() is called:")
    print("The original list:", end=" ")
    linked_list.printList()
    
    # Split the list into even and odd lists
    even_list, odd_list = linked_list.split()
    
    print("\nAfter split() was called:")
    print("The original list:", end=" ")
    linked_list.printList()
    
    print("The even list:", end=" ")
    even_list.printList()
    
    print("The odd list:", end=" ")
    odd_list.printList()
    
    # Clean up all lists
    linked_list.deleteList()
    even_list.deleteList()
    odd_list.deleteList()