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
    homeIndex = hash_func(key)
    curIndex = homeIndex

    while curIndex != -1:
        if hash_table[curIndex].indicator == USED and hash_table[curIndex].key == key:
            return -1
        curIndex = hash_table[curIndex].next
    
    if hash_table[homeIndex].indicator == EMPTY:
        hash_table[homeIndex].key = key
        hash_table[homeIndex].indicator = USED
        return homeIndex
    
    nextAvailableSlot = (homeIndex + 1) % TABLESIZE

    while nextAvailableSlot != homeIndex and hash_table[nextAvailableSlot].indicator == USED:
        nextAvailableSlot = (nextAvailableSlot + 1) % TABLESIZE

    if nextAvailableSlot == homeIndex:
        return TABLESIZE
    
    hash_table[nextAvailableSlot].key = key
    hash_table[nextAvailableSlot].indicator = USED

    curIndex = homeIndex
    while hash_table[curIndex].next != -1:
        curIndex = hash_table[curIndex].next
    
    hash_table[curIndex].next = nextAvailableSlot

    return nextAvailableSlot
    


def hash_find(key, hash_table):
    # Write your search logic here
    
    hashIndex = hash_func(key)
    curIndex = hashIndex

    while curIndex != -1:
        if hash_table[curIndex].indicator == USED and hash_table[curIndex].key == key:
            return curIndex
        curIndex = curIndex.next

    return -1



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