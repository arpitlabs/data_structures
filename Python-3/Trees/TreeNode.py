class TreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value
        
    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
      return self.left

    def get_right_child(self):
      return self.right
        
    def has_left_child(self):
        if self.left:
            return True
        else:
            return False
    
    def has_right_child(self):
        if self.right:
            return True
        else:
            return False
    
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"    