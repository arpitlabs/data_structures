from Trees.TreeNode import TreeNode 
from Trees.Tree import Tree 

class BinarySearchTree(Tree):
  def __init__(self, root_value = None):
    self.root = TreeNode(root_value)
  
  def insert(self, value):
    node = self.get_root()
    new_node = TreeNode(value)
    
    while True:
      if node.get_value() > value:
        if node.has_left_child():
          node = node.get_left_child()
        else:
          node.set_left_child(new_node)
          break;
      else:
        if node.has_right_child():
          node = node.get_right_child()
        else:
          node.set_right_child(new_node)
          break;
  
  # def search(self, value):
  #   node = 


