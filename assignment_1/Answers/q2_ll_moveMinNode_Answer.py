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
    # First find minimum value in list
    curr = head
    min_val = head.data
    while curr:
        if curr.data < min_val:
            min_val = curr.data
        curr = curr.next
    
    # If first node is already minimum and no other min nodes exist
    if head.data == min_val:
        curr = head.next
        prev = head
        # Check for other min nodes
        while curr:
            if curr.data == min_val:
                # Remove this min node
                prev.next = curr.next
                # Move it to front
                curr.next = head
                head = curr
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return head
    
    # Create new head for min nodes
    new_head = None
    last_min = None
    
    # Remove all min nodes and create new list with them
    dummy = Node(0)  # Dummy node to handle head changes
    dummy.next = head
    prev = dummy
    curr = head
    
    while curr:
        next_node = curr.next
        if curr.data == min_val:
            # Remove from original list
            prev.next = curr.next
            # Add to front of new list
            if not new_head:
                new_head = curr
                last_min = curr
            else:
                curr.next = new_head
                new_head = curr
        else:
            prev = curr
        curr = next_node
    
    # Connect min nodes list to rest of list
    last_min = new_head
    while last_min.next:
        last_min = last_min.next
    last_min.next = dummy.next
    
    return new_head
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