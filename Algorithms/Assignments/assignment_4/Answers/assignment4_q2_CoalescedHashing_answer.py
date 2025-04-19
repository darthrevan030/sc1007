TABLESIZE = 37
PRIME = 13
EMPTY = 0
USED = 1

class HashSlot:
    def __init__(self):
        self.key = 0
        self.indicator = EMPTY
        self.next = -1


def hash_func(key):
    return key % TABLESIZE


def hash_insert(key, hash_table):
    # Write your insertion logic here

    # Check if the key already exists in the hash table
    home_index = hash_func(key)
    current_index = home_index
    
    # Check if the key already exists in the hash table
    while current_index != -1:
        if hash_table[current_index].indicator == USED and hash_table[current_index].key == key:
            return -1  # Duplicate key
        current_index = hash_table[current_index].next
    
    # Key doesn't exist, so we can insert it
    # If home position is available, use it
    if hash_table[home_index].indicator == EMPTY:
        hash_table[home_index].key = key
        hash_table[home_index].indicator = USED
        return home_index
    
    # Home position is occupied, need to find the next available slot
    # Start from the home_index + 1 and wrap around if needed
    next_available = (home_index + 1) % TABLESIZE
    while next_available != home_index and hash_table[next_available].indicator == USED:
        next_available = (next_available + 1) % TABLESIZE
    
    if next_available == home_index:
        return TABLESIZE  # Table is full
    
    # Insert the key into the next available slot
    hash_table[next_available].key = key
    hash_table[next_available].indicator = USED
    
    # Now we need to link this to the chain
    # We follow the chain from the home position to the end
    current_index = home_index
    while hash_table[current_index].next != -1:
        current_index = hash_table[current_index].next
    
    # Link the last node to our new node
    hash_table[current_index].next = next_available
    
    return next_available

def hash_find(key, hash_table):
    # Write your search logic here
    hashed_index = hash_func(key)
    current_index = hashed_index
    
    # Traverse the chain to find the key
    while current_index != -1:
        if hash_table[current_index].indicator == USED and hash_table[current_index].key == key:
            return current_index  # Key found
        current_index = hash_table[current_index].next
    
    return -1  # Key not found


def print_menu():
    print("============= Hash Table ============")
    print("|1. Insert a key to the hash table  |")
    print("|2. Search a key in the hash table  |")
    print("|3. Print the hash table            |")
    print("|4. Quit                            |")
    print("=====================================")
    print("Enter selection: ", end="")


def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))

    hash_table = [HashSlot() for _ in range(TABLESIZE)]
    for slot in hash_table:
        slot.key = 0
        slot.indicator = EMPTY
        slot.next = -1

    i = 0
    print_menu()
    while i < len(data):

        opt = data[i]
        i += 1

        if opt == 1:  # Insert
            print("Enter a key to be inserted:")
            if i >= len(data):
                break
            key = data[i]
            i += 1
            index = hash_insert(key, hash_table)
            if index < 0:
                print("Duplicate key")
            elif index < TABLESIZE:
                print(f"Insert {key} at index {index}")
            else:
                print("Table is full.")
            print("Enter selection: ", end="")
        elif opt == 2:  # Search
            print("Enter a key for searching in the HashTable:")
            if i >= len(data):
                break
            key = data[i]
            i += 1
            index = hash_find(key, hash_table)
            if index != -1:
                print(f"{key} is found at index {index}.")
            else:
                print(f"{key} is not found.")
            print("Enter selection: ", end="")
        elif opt == 3:  # Print table
            print("index:\t key \t next")
            for j in range(TABLESIZE):
                print(f"{j}\t{hash_table[j].key}\t{hash_table[j].next}")
            print("Enter selection: ", end="")
        elif opt == 4:
            break
        else:
            print("Enter selection: ", end="")
            continue


if __name__ == "__main__":
    main()