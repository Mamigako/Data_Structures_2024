from node import Node
from NF_IE_exceptions import NotFoundException, ItemExistsException
from binary_tree_starter import BinaryTree

class BST(BinaryTree):

    def __init__(self) -> None:
        super().__init__()

    def _insert(self, key, data, node):

        if node == None:
            self.size += 1
            return Node(key, data)
        
        elif int(key) < int(node.key):
            node.left = self._insert(key, data, node.left)
            node.left.parent = node
        
        elif int(node.key) < int(key):
            node.right = self._insert(key, data, node.right)
            node.right.parent = node
        
        return node

    def insert(self, key, data):
    
        self.root = self._insert(key, data, self.root)

    def _update(self, key, data, node):

        if node == None:
            return None
        elif int(key) < int(node.key):
            return self._update(key, data, node.left)
        elif int(node.key) < int(key):
            return self._update(key, data, node.right)
        else:
            node.data = data

    def update(self, key, data):
        self._update(key, data, self.root)
        
    def _find(self, key, node):

        if node == None:
            return None
        
        elif int(key) < int(node.key):
            return self._find(key, node.left)

        elif int(node.key) < int(key):
            return self._find(key, node.right)
        else:
            return node
        
        return node

    def find(self, key):

        node = self._find(key, self.root)

        if node == None:
            raise NotFoundException()
        
        return node.data
                 
    def contains(self, key):
        
        if self._find(key, self.root) == None:
            return False
        else:
            return True


    def _remove(self, key, node):

        if node == None:
            return None
        if int(key) < int(node.key):
            node.left = self._remove(key, node.left)
        elif int(key) > int(node.key):
            node.right = self._remove(key, node.right)

        else:
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            
            successor = self._leftmost(node.right)

            node.key = successor.key
            node.data = successor.data

            node.right = self._remove(successor.key, node.right)

        return node

    def remove(self, key):
        self.root = self._remove(key, self.root)

    def _leftmost(self, node):
        
        current = node

        while current is not None:
            current = current.left
        
        return current

    def __setitem__(self, key, data):
        
        if self._update(key, data, self.root) == None:
            self.root = self._insert(key, data, self.root)
       
    def __getitem__(self, key):

        node = self._find(key, self.root)

        if node == None:
            raise NotFoundException()
        
        return node.data

    def __len__(self):
        return self.size

    def __str__(self) -> str:
        return self._recursive_printing(self.root)

