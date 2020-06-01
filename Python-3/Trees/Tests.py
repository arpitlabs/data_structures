from Trees.TreeNode import TreeNode
from Trees.Tree import Tree
from Trees.BinarySearchTree import BinarySearchTree

def run_tree():
  print()
  print("                      apple")
  print("                    /        \\")
  print("              banana           cherry")
  print("             /    \            /     \\")
  print("          dates   elderberry  figs   grapes")
  print()
  print(end="\n\n")

  tree = Tree("apple")
  tree.get_root().set_left_child(TreeNode("banana"))
  tree.get_root().set_right_child(TreeNode("cherry"))
  tree.get_root().get_left_child().set_left_child(TreeNode("dates"))
  tree.get_root().get_left_child().set_right_child(TreeNode("elderberry"))

  tree.get_root().get_right_child().set_left_child(TreeNode("figs"))
  tree.get_root().get_right_child().set_right_child(TreeNode("grapes"))

  print("pre-order: Node -> Left -> Right")
  print("-"*75)
  tree.pre_order(tree.root)
  print(end="\n\n\n")

  print()
  print("in-order: Left -> Node -> Right")
  print("-"*75)
  tree.in_order(tree.root)
  print(end="\n\n\n")

  print()
  print("post-order: Left -> Right -> Node")
  print("-"*75)
  tree.post_order(tree.root)
  print(end="\n\n\n")

  print()
  print("BFS (level order): Traverse all nodes at one level at a time, left to right")
  print("-"*75)
  tree.level_order()
  print(end="\n\n\n")

def run_binary_search_tree():
  tree = BinarySearchTree(5);
  tree.insert(4)
  tree.insert(2)
  tree.insert(6)

  print("pre-order:")
  tree.pre_order(tree.root)
  print()
  print()
  print("BFS (level order):")
  tree.level_order()
  print()

