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
    # Handle empty list or single node
    if not head or not head.next:
        return head
    
    # Find minimum value
    min_val = float('inf')
    curr = head
    while curr:
        if curr.data < min_val:
            min_val = curr.data
        curr = curr.next
    
    # Create new list starting with min nodes
    dummy = Node(0)  # Dummy node to help build result
    dummy_min = dummy  # Keep track of last min node
    curr = head
    
    # First move all min nodes to front
    while curr:
        if curr.data == min_val:
            dummy_min.next = Node(curr.data)
            dummy_min = dummy_min.next
        curr = curr.next
    
    # Then add all non-min nodes
    curr = head
    while curr:
        if curr.data != min_val:
            dummy_min.next = Node(curr.data)
            dummy_min = dummy_min.next
        curr = curr.next
        
    return dummy.next
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