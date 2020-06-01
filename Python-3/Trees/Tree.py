from Trees.TreeNode import TreeNode 
from Queues.Queue import Queue

class Tree:
    def __init__(self, root_value=None):
        self.root = TreeNode(root_value)
    
    def get_root(self):
        return self.root
    
    def pre_order(self, node):
      if node == None:
        return
      # parent -> left -> right
      print(node.get_value(), end = " -> ")
      self.pre_order(node.get_left_child())
      self.pre_order(node.get_right_child())

    def in_order(self, node):
      if node == None:
        return
      # left -> parent -> right
      self.in_order(node.get_left_child())
      print(node.get_value(), end = " -> ")
      self.in_order(node.get_right_child())
    
    def post_order(self, node):
      if node == None:
        return
      # left -> right -> parent 
      self.post_order(node.get_left_child())
      self.post_order(node.get_right_child())
      print(node.get_value(), end = " -> ")
    
    def level_order(self):
      visited = []
      queue = Queue()

      node = self.get_root()
      queue.enq(node)

      # dequeue next node and visit it
      while len(queue):
        node = queue.deq()
        print(node.get_value(), end = " -> ")

        # add its children to the queue
        if node.has_left_child():
          queue.enq(node.get_left_child())
        if node.has_right_child():
          queue.enq(node.get_right_child())
          
        

      #print(visited)