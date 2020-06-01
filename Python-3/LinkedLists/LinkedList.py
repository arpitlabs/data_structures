from LinkedLists.Node import Node

class LinkedList:

  def __init__(self, head):
    self.head = head

  def walk(self):
    current = self.head
    while current:
      print(current.data, end = ' -> ')
      current = current.next
    print('[end]')

  
  # insert
  def insert_at_begining(self, data):
    new_node = Node(data, head)
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
    else:
      last_item = self.head
      while last_item.next:
        last_item = last_item.next
      last_item.next = new_node
  
  def insert_after(self, data, node):
    if node is None:
      print("No node to insert after")
      return
    
    old_next_node = node.next
    new_node = Node(data, old_next_node)
    node.next = new_node
  
  def remove(self, node_data):
    if self.head is not None and self.head.data == node_data:
      self.head = self.head.next
      return
    
    prev = None
    current = self.head
    while current is not None:
      if current.data == node_data:
        break;
      prev = current
      current = current.next
    
    # point next of previous to next of current and remove current.
    if prev is not None:
      prev.next = current.next
    current = None

  def remove_all(self, node_data):
    if self.head is not None and self.head.data == node_data:
      self.head = self.head.next
    
    if self.head is None:
      return
    
    prev = None
    current = self.head
    while current is not None:
      if current.data == node_data:
        if prev is not None:
          prev.next = current.next
      prev = current
      current = current.next


  def remove_dups(self):
    # run two pointers - one in another iteratively 
    # comparing for duplicates
    # time O(N)
    # space O(N)
    runner = self.head

    while runner is not None:
      current = runner.next
      prev = runner
      while current is not None:
        if runner.data == current.data:
          prev.next = current.next
        else:
          prev = current
        current = current.next
      runner = runner.next
  
  def remove_dups_using_hash(self):
    # use a dictionary to mark items seen
    # time O(N)
    # space O(N)
    seen = { }
    prev = None
    current = self.head

    while current is not None:
      if current.data in seen:
        prev.next = current.next
      else:
        seen[current.data] = 1
        prev = current
      current = current.next
  
  def get_from_end(self, position_from_end):
    length = 0
    current = self.head
    while current is not None:
      current = current.next
      length += 1
    
    position_from_begining = length - position_from_end
    return self.get_from_begining(self.head, length, position_from_begining)
  
  def get_from_begining(self, head, length, position_from_begining):
    if position_from_begining == 0:
      return head.data
    return self.get_from_begining(head.next, length, position_from_begining - 1)


  def reverse(self):
    if self.head is None or self.head.next is None:
      return

    prev = None
    current = self.head
    next = self.head.next

    while current:
      next = current.next
      current.next = prev

      prev = current
      current = next
    
    self.head = prev

  def rev(self, prev, current):
    if current is None:
      self.head = prev
    else:
      self.rev(current, current.next)
      current.next = prev
  
  @staticmethod
  def sum_lists(list1, list2, s, sum_list):
    if list1.head is None and list2.head is None:
      return 0

    if list1.head:
      s += int(list1.head.data)
    if list2.head:
      s += int(list2.head.data)

    sum_list.insert_at_end(s%10)
    s = int(s/10)

    if list1.head:
      list1.head = list1.head.next
    if list2.head:
      list2.head = list2.head.next
    s +=  LinkedList.sum_lists(list1, list2, s, sum_list)
    return s

  def is_palindrome(self):
    # space: O(N)
    # time: O(N) + O(N/2) = O(N)
    list = []
    current = self.head
    while current:
      list.append(current.data)
      current = current.next
    
    i = 0
    l = len(list)
    while list[i] != list[l-1-i]:
      return False
    return True
  
  def has_loop(self):
    fast = self.head
    slow = self.head

    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next

      if slow == fast:
        return slow.next
    return None
  
  def pop(self):
    if self.head == None: 
      return None
    
    if self.head.next == None:
      current = self.head
      self.head = None
      return current

    prev = None
    current = self.head 
    while current.next: 
        prev = current
        current = current.next

    prev.next = None
    return current 



  



  









  




  