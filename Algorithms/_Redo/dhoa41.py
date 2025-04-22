def hash_insert(key, hash_table):
    # Write your code here

    # Double hashing implementation
    h1 = hash1(key)                    # Calculate the primary hash value (initial position)
    h2 = hash2(key)                    # Calculate the secondary hash value (step size)
    i = 0                              # Initialize probe sequence counter
    comparisons = 0                    # Initialize the counter for key comparisons
    insertion_index = -1               # Initialize the potential insertion position
    
    # First, check if the key already exists and find potential insertion point
    while i < TABLESIZE:               # Loop through all possible probe positions
        probe_index = (h1 + i * h2) % TABLESIZE  # Calculate current probe position using double hashing
        
        if hash_table[probe_index].indicator == USED:  # If slot is occupied
            comparisons += 1                           # Increment comparison counter
            if hash_table[probe_index].key == key:     # Check if the key already exists
                return -1                              # Return -1 for duplicate key
        elif hash_table[probe_index].indicator == EMPTY:  # If slot is empty
            # Found an empty slot and no duplicates so far
            if insertion_index == -1:                     # If no insertion point saved yet
                insertion_index = probe_index             # Save this as potential insertion point
            break                                         # Exit the loop - we know key isn't in table
        elif hash_table[probe_index].indicator == DELETED:  # If slot is marked as deleted
            # Found a deleted slot, can potentially insert here
            if insertion_index == -1:                       # If no insertion point saved yet
                insertion_index = probe_index               # Save as potential insertion point
        
        i += 1                         # Move to next probe position
    
    # If we've checked all slots and found no duplicates and no empty slots
    if i == TABLESIZE and insertion_index == -1:  # If table is full
        return TABLESIZE                          # Return TABLESIZE to indicate table is full
    
    # Insert the key
    hash_table[insertion_index].key = key             # Set the key
    hash_table[insertion_index].indicator = USED      # Mark the slot as used
    
    return comparisons                # Return the number of comparisons made


def hash_delete(key, hash_table):
    # Write your code here
    
    # Double hashing for deletion
    h1 = hash1(key)                    # Calculate the primary hash value
    h2 = hash2(key)                    # Calculate the secondary hash value
    i = 0                              # Initialize probe sequence counter
    comparisons = 0                    # Initialize comparison counter
    
    while i < TABLESIZE:               # Loop through all possible probe positions
        probe_index = (h1 + i * h2) % TABLESIZE  # Calculate probe position
        comparisons += 1                          # Increment comparison counter
        
        # If we find the key
        if hash_table[probe_index].indicator == USED and hash_table[probe_index].key == key:
            # Mark as DELETED instead of EMPTY to maintain probe chains
            hash_table[probe_index].indicator = DELETED    # Mark slot as deleted
            return comparisons                             # Return number of comparisons
        
        # If we hit an EMPTY slot, the key is not in the table
        if hash_table[probe_index].indicator == EMPTY:
            return -1                                     # Key not found
        
        # Continue probing
        i += 1                          # Move to next probe position
    
    # If we've probed the entire table and didn't find the key
    return -1                           # Key not found