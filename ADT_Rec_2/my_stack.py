from array_deque import ArrayDeque


class Stack:

    """Implementing the Stack ADT using an array based class."""
    
    def __init__(self):
        self.container = ArrayDeque()

    def push(self, data):
        return self.container.push_front(data)
    
    def pop(self):
        return self.container.pop_front()
    
    def get_size(self):
        return self.container.size

    def __str__(self):
        return self.container.__str__()

print("\nTESTING STACK\n")

stack = Stack()
stack.push(2)
stack.push(4)
stack.push(7)
print("the data structure is of size: " + str(stack.get_size()))
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("the data structure is of size: " + str(stack.get_size()))
