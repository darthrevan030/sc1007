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
    
    def dfs_count_all_words(node):
        """Count all words in the subtree rooted at node"""
        if not node:
            return 0
        
        words_count = 1 if node.is_end_of_word else 0
        
        # Process all children
        child = node.first_child
        while child:
            words_count += dfs_count_all_words(child)
            child = child.next_sibling
            
        return words_count
    
    def is_prefix_of(prefix, word):
        """Check if prefix is a prefix of word"""
        if len(prefix) > len(word):
            return False
        
        for i in range(len(prefix)):
            if prefix[i] != word[i]:
                return False
        return True
    
    def is_less_or_equal(s1, s2):
        """Check if s1 is lexicographically less than or equal to s2"""
        min_len = min(len(s1), len(s2))
        
        for i in range(min_len):
            if s1[i] < s2[i]:
                return True
            elif s1[i] > s2[i]:
                return False
        
        # If we've reached here, the first min_len characters are the same
        return len(s1) <= len(s2)
    
    def count_words_in_range(node, prefix, L, R):
        """
        Count words in the subtree rooted at node that are lexicographically
        between L and R (inclusive) and have the given prefix.
        """
        if not node:
            return
        
        current_word = prefix + node.char if node.char else prefix
        
        # Process the current node
        if node.is_end_of_word and current_word:
            if is_less_or_equal(L, current_word) and is_less_or_equal(current_word, R):
                count[0] += 1
        
        # Skip subtrees that can't contain words in the range
        child = node.first_child
        while child:
            next_word = current_word + child.char
            
            # If next_word could be <= R
            if is_less_or_equal(next_word, R) or is_prefix_of(next_word, R):
                # And if it's possible to have words >= L in this subtree
                if is_less_or_equal(L, next_word) or is_prefix_of(L, next_word) or is_less_or_equal(next_word, L):
                    count_words_in_range(child, current_word, L, R)
            
            child = child.next_sibling
    
    # Start the count from the root
    count_words_in_range(trie.root, "", L, R)
    
    return count[0]

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