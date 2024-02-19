"""Implementing a Singly Linked List Abstract Data Type using Python classes."""

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    
    def push_front(self, data):

        new_node = Node(data, self.head)

        if self.head != None:
            new_node.next = self.head

            node = new_node
            self.head = node
        else:
            self.head = new_node
        
        self.size += 1

    
    def pop_front(self):

        if self.head == None:
            return self.head

        elif self.head.next == None:
            pop_node = self.head
            self.size -= 1
            self.head = None
            return pop_node.data

        else:
            pop_node = self.head
            self.head = self.head.next
            self.size -= 1
            return pop_node.data
          

    def push_back(self, data):
        
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
            

    def pop_back(self):
        
        if self.size == 0:
            return None

        if self.head.next == None:
            curr_node = self.tail.data
            self.tail = None
            self.head = None
            self.size -= 1
            return curr_node
                 
        elif self.head.next == None:
            ret_node = self.head
            self.head = None
            self.size -= 1

            return ret_node

        else:
            curr_node = self.head
            
            while curr_node.next.next != None:
                curr_node = curr_node.next

            ret_node = curr_node.next
            
            self.tail = curr_node
            self.tail.next = None 
            self.size -= 1

            return ret_node.data


    def get_size(self):
        return self.size
        

    def __str__(self):
        
        ret_str = ""
        node = self.head
        
        while node != None:
            
            ret_str += str(node.data) + " " 
            node = node.next

        return ret_str



print("\nTESTING LINKED_LIST\n")

lis = LinkedList()
lis.push_back(3)
lis.push_back(1)
lis.push_back(6)
lis.push_back(9)
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_front())
print(lis.pop_front())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
lis.push_front(11)
lis.push_front(16)
lis.push_front(13)
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_front())
print(lis.pop_front())
print(lis.pop_back())
print(lis.pop_back())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_back())
print(lis.pop_front())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
