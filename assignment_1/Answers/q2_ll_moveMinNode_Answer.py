class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def findNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
        if self.head is None:
            raise ValueError("List is empty")
            
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur
        
    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")
            
        new_node = Node(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True
        
        prev_node = self.findNode(index - 1)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
        return True
    
    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

####################################################################################################################################################
def moveMinNode(head):
    # If list is empty or has only one node, no change needed
    if head is None or head.next is None:
        return head
        
    # Initialize variables to track minimum node and its previous node
    min_node = head
    min_prev = None
    curr_min = head.data
    
    # Variables for traversing the list
    prev = head
    curr = head.next
    
    # Find minimum node and its previous node
    while curr is not None:
        if curr.data < curr_min:
            curr_min = curr.data
            min_node = curr
            min_prev = prev
        prev = curr
        curr = curr.next
    
    # If minimum node is already at head, no change needed
    if min_prev is None:
        return head
        
    # Remove minimum node from its current position
    min_prev.next = min_node.next
    
    # Place minimum node at head
    min_node.next = head
    
    return min_node
####################################################################################################################################################

if __name__ == "__main__":
    linked_list = LinkedList()
    
    print("Enter a list of numbers, terminated by any non-digit character: ", end="")
    input_string = input()
    numbers = input_string.split()
    
    counter = 0
    for num in numbers:
        try:
            linked_list.insertNode(int(num), counter)
            counter += 1
        except ValueError:
            break
    
    print("\nBefore:", end=" ")
    linked_list.printList()
    
    linked_list.head = moveMinNode(linked_list.head)
    print("After:", end=" ")
    linked_list.printList()