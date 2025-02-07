class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

# Function to remove duplicates from a sorted linked list
def remove_duplicates_sorted_ll(ll):
    current = ll.head
    if current is None:
        return

    while current.next is not None:
        if current.item == current.next.item:
            temp = current.next.next
            current.next = temp
            ll.size -= 1
        else:
            current = current.next

def print_list(ll):
    current = ll.head
    if current is None:
        print("Empty")
        return

    while current is not None:
        print(current.item, end=" ")
        current = current.next
    print()

def remove_all_items(ll):
    current = ll.head
    while current is not None:
        temp = current.next
        current = None
        current = temp

    ll.head = None
    ll.size = 0

def find_node(ll, index):
    if ll is None or index < 0 or index >= ll.size:
        return None

    temp = ll.head
    while index > 0:
        temp = temp.next
        if temp is None:
            return None
        index -= 1

    return temp

def insert_node(ll, index, value):
    if ll is None or index < 0 or index > ll.size:
        return -1

    new_node = ListNode(value)

    # If inserting at the head
    if index == 0:
        new_node.next = ll.head
        ll.head = new_node
        ll.size += 1
        return 0

    # Insert at other positions
    prev_node = find_node(ll, index - 1)
    if prev_node is not None:
        new_node.next = prev_node.next
        prev_node.next = new_node
        ll.size += 1
        return 0

    return -1

def remove_node(ll, index):
    if ll is None or index < 0 or index >= ll.size:
        return -1

    # Remove head node
    if index == 0:
        ll.head = ll.head.next
        ll.size -= 1
        return 0

    # Remove other nodes
    prev_node = find_node(ll, index - 1)
    if prev_node is not None and prev_node.next is not None:
        prev_node.next = prev_node.next.next
        ll.size -= 1
        return 0

    return -1

if __name__ == "__main__":
    ll = LinkedList()

    while True:
        print("1: Insert an integer to the linked list:")
        print("2: Remove duplicates from a sorted linked list:")
        print("0: Quit:")
        choice = int(input("Please input your choice(1/2/0): "))

        if choice == 1:
            value = int(input("Input an integer that you want to add to the linked list: "))
            insert_node(ll, ll.size, value)
            print("The resulting linked list is: ")
            print_list(ll)
        elif choice == 2:
            remove_duplicates_sorted_ll(ll)
            print("The resulting linked list after removing duplicate values from the sorted linked list is: ")
            print_list(ll)
        elif choice == 0:
            remove_all_items(ll)
            break
        else:
            print("Choice unknown;")
