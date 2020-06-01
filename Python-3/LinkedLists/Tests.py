from LinkedLists.Node import Node
from LinkedLists.LinkedList import LinkedList
import LinkedLists.fnc 
      


# tests
def run():

  items = [[7,8,9],[3,5,7,12]]
  lists = [LinkedList(None) for i in range(len(items))]

  for i in range(len(items)):
    for j in range(len(items[i])):
      lists[i].insert_at_end(items[i][j])
  
  # inputs
  for i in range(len(lists)):
    lists[i].walk()
  
  merged = LinkedLists.fnc.merge(lists[0], lists[1])
  merged.walk()

  add_number = LinkedLists.fnc.add_number(lists[0], 1)
  add_number.walk()

  
  print("Test run complete")
