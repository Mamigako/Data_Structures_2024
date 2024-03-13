class BinaryTree:

    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def _populate_tree_recurring(self):
        
        key = input("Enter key: ")
        data = input("Enter data: ")

        if key == "":
            return None
        self.size += 1
        return Node(key, data, self._populate_tree_recurring(), self._populate_tree_recurring())
    
    def populate_tree(self):
        self.root = self._populate_tree_recurring()        
    
    def _recursive_printing(self, node):

        if node is None:
            return ""

        result = self._recursive_printing(node.left)
        result += f"{{{node.key}:{node.data}}} "
        result += self._recursive_printing(node.right)

        return result
