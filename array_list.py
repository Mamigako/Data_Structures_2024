class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self, capacity = 4, ordered_bool = False):
        self.capacity = capacity 
        self.size = 0  # Size will refer for the first available spot in the array
        self.array = [0]*self.capacity
        self.ordered_bool = ordered_bool

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        for element in range(self.size):
            if element == self.size - 1: # When we are at the last element
                    return_string += str(self.array[element])   
                    break 

            return_string += str(self.array[element]) + ", "

        return return_string
    
    def check_index_in_range(self, index, size_to_check):
        if (index < 0) or (index > size_to_check):
            raise IndexOutOfBounds()
        
        else:
            return True

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value): 
        self.insert(value, 0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        """
        We are going to loop backwards through the list after we checked that the index is in the range 
        and that the list is big enough, and we keep shiftng the items 1 spot forwards until we reach our index
        and then we insert the value there after we shifted the previous value.
        """
        if self.size == self.capacity: #In case the array is already full we need to resize it first
            self.resize()

        self.check_index_in_range(index, self.size) #If it doesn't raise an error then the function will just keep working

        for element in range(self.size, 0 , -1):
            if element != self.size: # so in case we have one last empty spot it doesn't switch the 0 to somewhere out of the array and throw an index error
                self.array[element + 1] = self.array[element]

            if self.size == index:
                self.array[index] = value
                self.size += 1 # when the insert is done successfully we need to increase our size by 1
                break   #So we don't keep going and shifting the rest of the elements
        
        self.check_if_ordered()

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.insert(value, self.size)

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        self.check_index_in_range(index, self.size) #If it doesn't raise an error then the function will just keep working
        self.array[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        self.get_at(0)

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if self.size != 0:    # So the list is not empty
            self.check_index_in_range(index, self.size - 1) #If it doesn't raise an error then the function will just keep working
            return self.array[index]
        
        else: 
            raise Empty()

    #Time complexity: O(1) - constant time
    def get_last(self):
        self.get_at(self.size - 1)

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.capacity *= 2
        temp_array = self.array
        self.array = [0]*self.capacity

        for index in range(self.size):
            self.array[index] = temp_array[index]

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if self.size != 0:
            self.check_index_in_range(index, self.size - 1)

            for element in range(index, self.size):
                self.array[index] = 0

                if index != self.size - 1: # So in case we weren't removing the last element in a "FULL" array and we need to shift the further elements one position back
                    self.array[element] = self.array[element + 1]

            self.size -= 1

        else:
            raise Empty()

    #Time complexity: O(1) - constant time
    def clear(self):
        self. array =  [0]*self.capacity

    def check_if_ordered(self):
        try:
            if self.size > 1:
                for index in range(1, self.size):
                    if self.array[index] < self.array[index - 1]:
                        self.ordered_bool = False
                        break
                    
                    self.ordered_bool = True

            else:
                self.ordered_bool = True
                

        except TypeError:
            self.ordered_bool = False

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        self.check_if_ordered()
        if self.ordered_bool:
            the_wanted_index = 0
            
            for index in range(self.size):
                if self.array[index] <= value:
                    the_wanted_index = index   # So it will keep re-assigning the wanted index to insert the value for every element until it find an element that is greater than the value

            self.insert(value, the_wanted_index + 1)

        else:
            raise NotOrdered()

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    print(str(arr_lis))