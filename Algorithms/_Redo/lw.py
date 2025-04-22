def find_longest_word_iterative(trie):
    if not trie.root.first_child:
        return None  # Empty trie
    
    longest_word = ""
    stack = []
    
    # Add all first-level children to stack
    child = trie.root.first_child
    while child:
        stack.append((child, child.char))
        child = child.next_sibling
    
    while stack:
        node, word_so_far = stack.pop()
        
        if node.is_end_of_word and len(word_so_far) > len(longest_word):
            longest_word = word_so_far
        
        # Add all children to stack
        child = node.first_child
        while child:
            stack.append((child, word_so_far + child.char))
            child = child.next_sibling
    
    return longest_word if longest_word else None

def find_longest_word(trie):
    if not trie.root.first_child:
        return None  # Empty trie
    
    longest_word = ""
    
    def dfs(node, current_word):
        nonlocal longest_word
        
        # If this is a complete word, check if it's longer than our current longest
        if node.is_end_of_word and len(current_word) > len(longest_word):
            longest_word = current_word
        
        # Visit all children
        child = node.first_child
        while child:
            dfs(child, current_word + child.char)
            child = child.next_sibling
    
    # Start DFS from the root (with empty word)
    dfs(trie.root, "")
    
    return longest_word if longest_word else None