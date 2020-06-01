from LinkedLists.Node import Node
from LinkedLists.LinkedList import LinkedList

class Stack:
  def __init__(self):
    self.storage = LinkedList(None)
    self.last_item = None
    self.item_counter = 0
    self.min = None
  
  def __len__(self):
    return self.item_counter
  
  def push(self, item):
    head = self.storage.head
    if head is None:
      self.storage.head = Node(item)
    else:
      new_node = Node(item)
      new_node.next = head
      self.storage.head = new_node
    self.last_item = item
    self.item_counter += 1

    if self.min is None:
      self.min = item
    elif  self.min > item:
      self.min = item
    #self.storage.walk()
    #print(self.item_counter)

  def pop(self):

    if self.item_counter > 0:
      head = self.storage.head
      if head is not None:
        next = head.next
        self.storage.head = next
        return head.data
    else:
      print("Stack is empty")
      return None
  
  def top(self):
    self.storage.walk()
    return self.last_item
  
  def reverse(self):
    print(self.storage.head.data)
    self.storage.reverse()
    print(self.storage.head.data)
    self.last_item = self.storage.head.data

  def minimum(self):
    return self.min




  

