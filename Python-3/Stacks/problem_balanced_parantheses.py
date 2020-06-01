from Stacks.Stack import Stack
from Stacks.StackUsingArray import StackUsingArray

# Take a mathematical expression as a string input and return True if it's parentheses are balanced or False if it is not. 

def has_balanced_parantheses(expression):
  stack = Stack()
  if expression:
    for char in expression:
      print(char)
      if char == "(":
        stack.push(char)
      elif char == ")":
        if stack.pop() == None:
          return False
  
  if len(stack) == 0:
    return True
  return False


def run():
  print(has_balanced_parantheses("((3^2 + 8)x(5/2))/(2+6)"))

