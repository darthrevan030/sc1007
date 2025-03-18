class BTNode():
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def preOrderTraversal(self, node):
        if node:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)
    
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")

    def level_order_traversal(self): # using queue
        if not self.root:
            return
        
        queue = Queue()
        queue.enqueue(self.root)
        
        while not queue.is_empty():
            current_node = queue.dequeue()
            print(current_node.data, end=" ")
        
        if current_node.left:
            queue.enqueue(current_node.left)
        
        if current_node.right:
            queue.enqueue(current_node.right)