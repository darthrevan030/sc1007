class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # Add to the end

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove from the front
        return None

    def is_empty(self):
        return len(self.items) == 0

class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.first_child = None
        self.next_sibling = None
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _find_child(self, node, char):
        prev = None
        curr = node.first_child
        while curr and curr.char < char:
            prev = curr
            curr = curr.next_sibling
        if curr and curr.char == char:
            return curr
        return None

    def _insert_child(self, node, char):
        prev = None
        curr = node.first_child
        while curr and curr.char < char:
            prev = curr
            curr = curr.next_sibling

        if curr and curr.char == char:
            return curr  # already exists

        new_node = TrieNode(char)
        new_node.next_sibling = curr
        if prev:
            prev.next_sibling = new_node
        else:
            node.first_child = new_node
        return new_node

    def insert(self, word):
        current = self.root
        for char in word:
            child = self._insert_child(current, char)
            current = child
        current.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            node = self._find_child(node, char)
            if not node:
                return False  # Character path not found
        return node.is_end_of_word


def count_in_range(trie, L, R):
    #write you codes here
    """
    Count words in the trie that are lexicographically between L and R (inclusive).
    """
    count = [0]  # Using a list to allow modification in nested functions
    
    def is_between(word, L, R):
        """Check if word is lexicographically between L and R (inclusive)"""
        return L <= word <= R           # Using Python's string comparison
    
    def dfs(node, prefix):
        """Depth-first search to count words in range"""
        if not node:                    # Base case: null node
            return
        
        current_word = prefix + node.char if node.char else prefix  # Build current word
        
        # If we've found a complete word, check if it's in the range
        if node.is_end_of_word and current_word:    # If this is a complete word
            if is_between(current_word, L, R):      # Check if it's in the range
                count[0] += 1                       # Increment count
        
        # Recursively explore all children
        child = node.first_child                    # Get first child
        while child:                                # For each child
            # Early pruning: only explore branches that could lead to words in range
            next_word = current_word + child.char   # Build next possible word
            
            # If next_word could be <= R (i.e., in range or a prefix of words in range)
            if next_word <= R:                      # If still within upper bound
                # And if it's possible to have words >= L in this subtree
                if L <= next_word or L.startswith(next_word):  # If potentially above lower bound
                    dfs(child, current_word)        # Recursively explore this branch
            
            child = child.next_sibling              # Move to next sibling
    
    # Start the traversal from the root with an empty prefix
    dfs(trie.root, "")                  # Start DFS from root
    
    return count[0]                     # Return the final count

#Read input
n, q = map(int, input().split())
trie = Trie()

# Insert words
for _ in range(n):
    word = input().strip()
    trie.insert(word)

# Process queries
for _ in range(q):
    L, R = input().strip().split()
    print(count_in_range(trie, L, R))