from LinkedLists.Node import Node
from LinkedLists.LinkedList import LinkedList


def merge(list1, list2):
  p1 = list1.head
  p2 = list2.head

  result = LinkedList(None)

  while p1 and p2:
    if p1.data > p2.data:
      result.insert_at_end(p2.data)
      p2 = p2.next
    else:
      result.insert_at_end(p1.data)
      p1 = p1.next
  
  if p1 is None:
    while p2:
      result.insert_at_end(p2.data)
      p2 = p2.next
  
  if p2 is None:
    while p1:
      result.insert_at_end(p1.data)
      p1 = p1.next
  
  return result

def add_number(list1, number):
  list1.rev(None, list1.head)
  
  result = LinkedList(None)
  current = list1.head
  s = int(current.data) + int(number)
  
  result.insert_at_end(s%10)
  carry = int(s/10)
  
  current = current.next
  while current:
    s = carry + int(current.data)
    result.insert_at_end(s%10)
    carry = int(s/10)
    current = current.next
  
  result.rev(None, result.head)
  return result




