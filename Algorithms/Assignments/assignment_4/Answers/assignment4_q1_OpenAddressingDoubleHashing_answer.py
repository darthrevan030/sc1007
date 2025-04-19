TABLESIZE = 37
PRIME = 13
EMPTY = 0
USED = 1
DELETED = 2

class HashSlot:
    def __init__(self):
        self.key = 0
        self.indicator = EMPTY

def hash1(key):
    return key % TABLESIZE

def hash2(key):
    return (key % PRIME) + 1


def hash_insert(key, hash_table):
    # Write your code here

    # Double hashing implementation
    h1 = hash1(key)
    h2 = hash2(key)
    i = 0
    comparisons = 0
    insertion_index = -1
    
    # First, check if the key already exists and find potential insertion point
    while i < TABLESIZE:
        probe_index = (h1 + i * h2) % TABLESIZE
        
        if hash_table[probe_index].indicator == USED:
            comparisons += 1
            if hash_table[probe_index].key == key:
                return -1  # Duplicate key
        elif hash_table[probe_index].indicator == EMPTY:
            # Found an empty slot and no duplicates so far
            if insertion_index == -1:
                insertion_index = probe_index
            break
        elif hash_table[probe_index].indicator == DELETED:
            # Found a deleted slot, can potentially insert here
            if insertion_index == -1:
                insertion_index = probe_index
        
        i += 1
    
    # If we've checked all slots and found no duplicates and no empty slots
    if i == TABLESIZE and insertion_index == -1:
        return TABLESIZE  # Table is full
    
    # Insert the key
    hash_table[insertion_index].key = key
    hash_table[insertion_index].indicator = USED
    
    return comparisons


def hash_delete(key, hash_table):
    # Write your code here
    
    # Double hashing for deletion
    h1 = hash1(key)
    h2 = hash2(key)
    i = 0
    comparisons = 0
    
    while i < TABLESIZE:
        probe_index = (h1 + i * h2) % TABLESIZE
        comparisons += 1
        
        # If we find the key
        if hash_table[probe_index].indicator == USED and hash_table[probe_index].key == key:
            # Mark as DELETED instead of EMPTY to maintain probe chains
            hash_table[probe_index].indicator = DELETED
            return comparisons
        
        # If we hit an EMPTY slot, the key is not in the table
        if hash_table[probe_index].indicator == EMPTY:
            return -1
        
        # Continue probing
        i += 1
    
    # If we've probed the entire table and didn't find the key
    return -1


def print_menu():
    print("============= Hash Table ============")
    print("|1. Insert a key to the hash table  |")
    print("|2. Delete a key from the hash table|")
    print("|3. Print the hash table            |")
    print("|4. Quit                            |")
    print("=====================================")
    print("Enter selection: ", end="")

def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))

    hash_table = [HashSlot() for _ in range(TABLESIZE)]
    i = 0
    print_menu()
    while i < len(data):
        opt = data[i]
        i += 1

        if opt == 1:
            print("Enter a key to be inserted:")
            if i >= len(data):
                break
            key = data[i]
            i += 1
            comparison = hash_insert(key, hash_table)
            if comparison < 0:
                print("Duplicate key")
            elif comparison < TABLESIZE:
                print(f"Insert: {key} Key Comparisons: {comparison}")
            else:
                print(f"Key Comparisons: {comparison}. Table is full.")
            print("Enter selection: ", end="")
        elif opt == 2:
            print("Enter a key to be deleted:")
            if i >= len(data):
                break
            key = data[i]
            i += 1
            comparison = hash_delete(key, hash_table)
            if comparison < 0:
                print(f"{key} does not exist.")
            elif comparison <= TABLESIZE:
                print(f"Delete: {key} Key Comparisons: {comparison}")
            else:
                print("Error")
            print("Enter selection: ", end="")
        elif opt == 3:
            for j in range(TABLESIZE):
                marker = '*' if hash_table[j].indicator == DELETED else ' '
                print(f"{j}: {hash_table[j].key} {marker}")
            print("Enter selection: ", end="")
        elif opt == 4:
            break
        else:
            continue


if __name__ == "__main__":
    main()

