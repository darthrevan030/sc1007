def dfs_traversal(trie):
    """
    Performs a depth-first traversal of the trie and returns words with their lengths.
    Useful for multiple scenarios like finding longest words or all words in the trie.
    """
    if not trie.root.first_child:
        return []  # Empty trie
    
    result = []
    
    def dfs_helper(node, word_so_far):
        if node.is_end_of_word:
            result.append((word_so_far, len(word_so_far)))
        
        # Visit all children
        child = node.first_child
        while child:
            dfs_helper(child, word_so_far + child.char)
            child = child.next_sibling
    
    # Start DFS from the root (with empty word)
    dfs_helper(trie.root, "")
    
    return result