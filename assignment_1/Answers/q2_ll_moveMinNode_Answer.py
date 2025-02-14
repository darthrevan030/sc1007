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
    
    # Find minimum value in a single pass
    min_val = head.data
    curr = head.next
    while curr:
        if curr.data < min_val:
            min_val = curr.data
        curr = curr.next
    
    # If no min nodes need to be moved (head is min and no other mins)
    if head.data == min_val and head.next.data != min_val:
        return head
    
    # Create new head for min nodes
    new_head = None
    
    # Handle all nodes in a single pass
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    
    while curr:
        if curr.data == min_val:
            # Remove from current position
            prev.next = curr.next
            # Move to front
            curr.next = new_head
            new_head = curr
            curr = prev.next
        else:
            prev = curr
            curr = curr.next
    
    # Connect min nodes to rest of list
    curr = new_head
    while curr.next:
        curr = curr.next
    curr.next = dummy.next
    
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