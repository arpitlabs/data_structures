from Stacks.Stack import Stack

def run():
  expression = "3 1 + 4 *"
  operands = Stack();

  for char in expression.split(' '):
    if char == "*":
      op2 = operands.pop()
      op1 = operands.pop()
      output = int(op1) * int(op2)
      operands.push(output)
    elif char == "/":
      op2 = operands.pop()
      op1 = operands.pop()
      output = int(op1) / int(op2)
      operands.push(output)
    elif char == "+":
      op2 = operands.pop()
      op1 = operands.pop()
      output = int(op1) + int(op2)
      operands.push(output)
    elif char == "-":
      op2 = operands.pop()
      op1 = operands.pop()
      output = int(op1) - int(op2)
      operands.push(output)
    else:
      operands.push(char)
  print(operands.pop())
    


