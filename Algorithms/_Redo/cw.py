def count_words_bfs(trie):
    count = 0
    queue = Queue()
    queue.enqueue(trie.root)
    
    while not queue.is_empty():
        node = queue.dequeue()
        
        if node.is_end_of_word:
            count += 1
        
        # Add all children to queue
        child = node.first_child
        while child:
            queue.enqueue(child)
            child = child.next_sibling
    
    return count

def count_words(trie):
    def count_recursive(node):
        count = 0
        
        # Count this node if it's end of a word
        if node.is_end_of_word:
            count += 1
        
        # Count words in child nodes
        child = node.first_child
        while child:
            count += count_recursive(child)
            child = child.next_sibling
            
        return count
    
    return count_recursive(trie.root)