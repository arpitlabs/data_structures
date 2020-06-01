from Stacks.StackUsingArray import StackUsingArray
from Stacks.Stack import Stack
import Stacks.problem_balanced_parantheses

def run():
  #Stacks.problem_balanced_parantheses.run()
  stack  = Stack()
  for i in range(10):
    stack.push(i + 1)
  
  for i in range(10):
    stack.pop()
  
  print(stack.minimum())
  

