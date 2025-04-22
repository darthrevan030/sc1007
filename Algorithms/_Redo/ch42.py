def hash_insert(key, hash_table):
    # Write your insertion logic here

    # Check if the key already exists in the hash table
    home_index = hash_func(key)         # Calculate the home position for the key
    current_index = home_index          # Start at the home position
    
    # Check if the key already exists in the hash table
    while current_index != -1:          # While not at the end of the chain
        if hash_table[current_index].indicator == USED and hash_table[current_index].key == key:
            return -1                    # Duplicate key found, return -1
        current_index = hash_table[current_index].next  # Move to next node in chain
    
    # Key doesn't exist, so we can insert it
    # If home position is available, use it
    if hash_table[home_index].indicator == EMPTY:   # If home position is empty
        hash_table[home_index].key = key            # Insert key at home position
        hash_table[home_index].indicator = USED     # Mark slot as used
        return home_index                           # Return insertion index
    
    # Home position is occupied, need to find the next available slot
    # Start from the home_index + 1 and wrap around if needed
    next_available = (home_index + 1) % TABLESIZE   # Start looking at next position
    while next_available != home_index and hash_table[next_available].indicator == USED:
        next_available = (next_available + 1) % TABLESIZE  # Move to next position
    
    if next_available == home_index:                # If we've checked all positions
        return TABLESIZE                            # Table is full
    
    # Insert the key into the next available slot
    hash_table[next_available].key = key            # Insert key at found position
    hash_table[next_available].indicator = USED     # Mark slot as used
    
    # Now we need to link this to the chain
    # We follow the chain from the home position to the end
    current_index = home_index                      # Start at home position
    while hash_table[current_index].next != -1:     # Find the end of the chain
        current_index = hash_table[current_index].next  # Move to next node
    
    # Link the last node to our new node
    hash_table[current_index].next = next_available  # Link to new node
    
    return next_available                           # Return insertion index

def hash_find(key, hash_table):
    # Write your search logic here
    hashed_index = hash_func(key)       # Calculate the home position
    current_index = hashed_index        # Start at the home position
    
    # Traverse the chain to find the key
    while current_index != -1:          # While not at the end of the chain
        if hash_table[current_index].indicator == USED and hash_table[current_index].key == key:
            return current_index         # Key found, return its index
        current_index = hash_table[current_index].next  # Move to next node in chain
    
    return -1                          # Key not found