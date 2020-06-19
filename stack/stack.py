"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        #add element to the front of the array
        self.size += 1
        self.storage.add_to_head(value)
        
    def pop(self):
        # check if empty
        if self.__sizeof__ == 0:
            return None
        # remove first element in storage
        self.size -= 1
        node = self.storage.remove_head() 
        return node  
