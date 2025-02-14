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

    def removeNode(self, index):
        if self.head is None:
            raise ValueError("List is empty")
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
            
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
            
        pre = self.findNode(index - 1)
        if pre.next is not None:
            pre.next = pre.next.next
            self.size -= 1
            return True
        return False

    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end="  ")
            cur = cur.next
        print("")

class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, data):    
        try:
            self.ll.insertNode(data, 0)
        except ValueError as e:
            print(e)

    def pop(self):
        if self.isEmpty():
            return None
        data = self.ll.head.data    
        try:
            self.ll.removeNode(0)
        except ValueError as e:
            print(e)
            return None
        return data

    def peek(self):
        if self.isEmpty():
            return None
        return self.ll.head.data    

    def isEmpty(self):
        return self.ll.size == 0

    def getSize(self):
        return self.ll.size

    def printStack(self):
        self.ll.printList()

####################################################################################################################################################
def deleteMiddleElement(s):
    if s.isEmpty():
        return
        
    # Get stack size and calculate middle position
    size = s.getSize()
    middle = size // 2  # Integer division gives us lower middle for even numbers
    
    # Create temporary stack
    temp = Stack()
    
    # Move elements to temporary stack until we reach middle
    for i in range(size - middle - 1):
        temp.push(s.pop())
        
    # Remove middle element
    s.pop()
    
    # Restore elements from temporary stack
    while not temp.isEmpty():
        s.push(temp.pop())
    return
####################################################################################################################################################

if __name__ == "__main__":
    s = Stack()

    print("Enter a list of numbers, terminated by any non-digit character: ", end="")
    input_string = input()
    numbers = input_string.split()

    counter = 0
    for num in numbers:
        try:
            s.push(int(num))
        except ValueError:
            break

    print("\nBefore:", end=" ")
    s.printStack()

    deleteMiddleElement(s)

    print("After:", end=" ")
    s.printStack()