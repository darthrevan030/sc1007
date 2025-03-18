class BTNode():
    
    def count_nodes(self, node):
        if not node:
            return 0
    
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
    
    def calculate_height(self, node):
        if node is None:
            return -1
        
        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)
        
        return 1 + max(left_height, right_height)
    
    def insert(self, data):
        if self.root is None:
            self.root = BTNode(data)
        else:
            self._insert(data, self.root)

    def _search(self, data, current_node):
        if current_node is None:
            return False
        elif data == current_node.data:
            return True
        elif data < current_node.data:
            return self._search(data, current_node.left)
        else:
            return self._search(data, current_node.right)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = BTNode(data)
            else:
                self._insert(data, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = BTNode(data)
            else:
                self._insert(data, current_node.right)

