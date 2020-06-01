# Reverse a string
reverse_string = lambda string_to_reverse: "".join(string_to_reverse[::-1])
print(reverse_string("Arpit Khandelwal"))

# Find Palindrome
palindrome = lambda string: string == reverse_string(string)
print(palindrome("tyeyt"))

# Alternate solution Palindrome
def palindrome(string):
  rev_counter = -1
  for char in string:
    if char != string[rev_counter]:
      return False
    else:
      rev_counter -= 1
  return True

# Reverse a number
def reverse_number(number):
  negative = number < 0
  multiplier = 1
  if negative:
    multiplier = -1
  
  number = number * multiplier
  reversed_string = reverse_string(str(number))
  reversed_int = int(reversed_string) * multiplier

  return reversed_int

# given a string, return the character that most
# commonly used in the string
def max_occuring_char(string):
  original_length = len(string)
  new_length = original_length
  new_char = ''

  for char in string:
    if len(string.replace(char, '', -1)) < new_length:
      new_length = len(string.replace(char, '', -1))
      new_char = char
  
  return new_char, (original_length - new_length)

# given a string, return the character that most
# commonly used in the string
def build_char_map(string):
  char_map = {char: 0 for char in string }
  for char in string:
    char_map[char] = char_map[char] + 1
  return char_map

def another_max_occuring_char(string):
  char_map = build_char_map(string)
  counter = 0;
  max_occuring_char = ''

  for char in char_map.keys():
    if char_map[char] > counter:
      counter = char_map[char]
      max_occuring_char = char

  return max_occuring_char, counter

# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print “Fizz” instead of the number 
# and for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three and five print “FizzBuzz”.
def fizz_buzz():
  for number in range(1, 101):
    if number % 15 == 0:
      print('fizzbuzz')
    elif number % 3 == 0:
      print('fizz')
    elif number % 5 == 0:
      print('buzz')
    else:
      print(number)

# array chunking
def get_slice(array, start_index, stop_index):
  # python specific solution
  # chunk = array[start_index:stop_index]
  # for i in chunk:
  #     array.remove(i)
  # return array, chunk

  # generic solution
  chunk = []
  for i in range(start_index, stop_index):
    if not array: # list is empty
      break
    chunk.append(array.pop(0))
  return array, chunk

def chunk(array, chunk_size):
  list_of_chunks = []
  while array: # unless list is empty
    array, chunk = get_slice(array, 0, chunk_size)
    list_of_chunks.append(chunk)
  
  return list_of_chunks
