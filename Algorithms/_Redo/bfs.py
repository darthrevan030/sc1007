def bfs_traversal(trie):
    """
    Performs a breadth-first traversal of the trie and returns words with their lengths.
    Useful for multiple scenarios like finding shortest/longest words or words of specific lengths.
    """
    if not trie.root.first_child:
        return []  # Empty trie
    
    result = []
    queue = Queue()
    
    # Add all first-level children to queue with their character
    child = trie.root.first_child
    while child:
        queue.enqueue((child, child.char))
        child = child.next_sibling
    
    # BFS
    while not queue.is_empty():
        node, word_so_far = queue.dequeue()
        
        if node.is_end_of_word:
            result.append((word_so_far, len(word_so_far)))
        
        # Add all children to queue
        child = node.first_child
        while child:
            queue.enqueue((child, word_so_far + child.char))
            child = child.next_sibling
    
    return result