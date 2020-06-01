class StackUsingArray:
  

  def __init__(self):
    self.array = [0 for i in range(10)]
    self.next_index = 0
  
  def push(self, item):
    if self.next_index == len(self.array):
      print("capacity reached")
      self.expand()
    self.array[self.next_index] = item
    self.next_index += 1
  
  def pop(self):
    if self.next_index == 0:
      print("Stack is empty")
      return None

    last_index = self.next_index - 1
    last = self.array[last_index];
    self.array[last_index] = 0
    self.next_index -= 1
    return last

  def __len__(self):
    return self.next_index

  def expand(self):
    print("expanding")
    new_array = [0 for _ in range((len(self.array) * 2))]
    for index, element in enumerate(self.array):
      new_array[index] = element
    self.array = new_array

