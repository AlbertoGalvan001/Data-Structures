"""class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node
  
class LinkedList:
  def __init__(self):
    self.head = None # Stores a node, that corresponds to our first node in the list 
    self.tail = None # stores a node that is the end of the list

  def __str__(self):
    output = ''
    current_node = self.head  #create tracker node (loops through linked list)
    while current_node is not None: # loop until its none

      output += f'{current_node.value} ->' 

    current_node = current_node.next_node   #update the tracker node to next node
  
  def add_to_tail(self, value):
    # create a node to add
    new_node = Node(value)
    # check if list is empty
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      # point the node at the current tail, to the new node
      self.tail.next_node = new_node
      self.tail = new_node

  def contains(self, value):
    if self.head is None:
      return False
    
    # Loop through each node, until we see the value, or we cannot go further
    current_node = self.head
    while current_node is not None:
      # check if this is the node we are looking for
      if current_node.value == value:
        return True
      # otherwise, go to the next node
      current_node = current_node.next_node
      return False 

  # remove the head and return its value
  def remove_head(self):
    # if list is empty, do nothing
    if not self.head:
      return None
    # if list only has one element, set head and tail to None
    if self.head.next_node is None:
      head_value = self.head.value
      self.head = None
      self.tail = None
      return head_value
    # otherwise we have more elements in the list
    head_value = self.head.value
    self.head = self.head.next_node
    return head_value 
​          
  def get_max(self):
    #if list is empty, do nothing
    if not self.head:
        return None:

    #if list only has one element, set to only value
    if self.head == self.tail
        return self.head.value  

    # loop through each node 
    current_node = self.head
    # establish an incramental value
    incrament = 0
    # track the max value
    max_value = 0

    #incrament to mark our index through the length of list
    while incrament < self.length:
        #add 1 to the incrament
        incrament += 1
        # if max_value is less than current nodes value, set max value to it.
        if max_value < current_node.value:
            max_value = current_node.value
        #set current node to the next node and repeat.    
        current_node = current_node.next_node

    #once all nodes have been checked, return max_value
    return max_value """
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node
  

class LinkedList:
  def __init__(self):
    # Stores a node, that corresponds to our first node in the list 
    self.head = None     
    # stores a node that is the end of the list
    self.tail = None 
  
  # return all values in the list a -> b -> c -> d -> None
  def __str__(self):
    output = ''
    current_node = self.head # create a tracker node variable
    while current_node is not None: # loop until its NONE

      output += f'{current_node.value} -> '

      current_node = current_node.next_node # update the tracker node to the next node

    return output
  def add_to_head(self, value):
    # create a node to add
    new_node = Node(value)
    # check if list is empty
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      # new_node should point to current head
      new_node.next_node = self.head
      # move head to new node
      self.head = new_node

  def add_to_tail(self, value):
    # create a node to add
    new_node = Node(value)
    # check if list is empty
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      # point the node at the current tail, to the new node
      self.tail.next_node = new_node
      self.tail = new_node

  # remove the head and return its value
  def remove_head(self):
    # if list is empty, do nothing
    if not self.head:
      return None
    # if list only has one element, set head and tail to None
    if self.head.next_node is None:
      head_value = self.head.value
      self.head = None
      self.tail = None
      return head_value
    # otherwise we have more elements in the list
    head_value = self.head.value
    self.head = self.head.next_node
    return head_value 

  def contains(self, value):
    if self.head is None:
      return False
    
    # Loop through each node, until we see the value, or we cannot go further
    current_node = self.head

    while current_node is not None:
      # check if this is the node we are looking for
      if current_node.value == value:
        return True

      # otherwise, go to the next node
      current_node = current_node.next_node
    return False 
  
  def get_max(self):
    #if list is empty, do nothing
    if not self.head:
        return None

    #if list only has one element, set to only value
    if self.head == self.tail:
        return self.head.value  

    # loop through each node 
    current_node = self.head
    # establish an incramental value
    incrament = 0
    # track the max value
    max_value = 0

    #incrament to mark our index through the length of list
    while incrament < self.length:
        #add 1 to the incrament
        incrament += 1
        # if max_value is less than current nodes value, set max value to it.
        if max_value < current_node.value:
            max_value = current_node.value
        #set current node to the next node and repeat.    
        current_node = current_node.next_node

    #once all nodes have been checked, return max_value
    return max_value 