class NotFoundException(Exception):
    def __init__(self, message="Item not found."):
        self.message = message
        super().__init__(self.message)

class ItemExistsException(Exception):
    def __init__(self, message="Item already exists."):
        self.message = message
        super().__init__(self.message)
