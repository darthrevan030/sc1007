def find_shortest_word_with_prefix(self, prefix):
    #Step 1: Traverse to the end of the prefix    
    node = self.root    
    for char in prefix:
        node = self._find_child(node, char)    
        if not node:
            return None
    
    # Step 2: BFS    
    queue = Queue()
    queue.enqueue((node, prefix))
    while not queue.is_empty():
        current_node, path = queue.dequeue()
        if current_node.is_end_of_word:
            return path        
        child = current_node.first_child       
    
    while child:
        queue.enqueue((child,path+child.char))
        child = child.next_sibling        
        
    return None

def find_shortest_word(trie):
    if not trie.root.first_child:
        return None  # Empty trie
    
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
            return word_so_far  # Found the shortest word
        
        # Add all children to queue
        child = node.first_child
        while child:
            queue.enqueue((child, word_so_far + child.char))
            child = child.next_sibling
    
    return None  # No word found (shouldn't happen if trie has words)