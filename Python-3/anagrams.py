import re

# anagram
def build_char_map(string):
  # remove any special characters from the string
  string = re.sub("[^\w]", "", string)
  char_map = {char.lower(): 0 for char in string }
  for char in string:
    char = char.lower()
    char_map[char] = char_map[char] + 1
  return char_map

def anagrams(str1, str2):
  c_map1 = build_char_map(str1)
  c_map2 = build_char_map(str2)

  if len(c_map1.keys()) != len(c_map2.keys()):
    return False

  for key in c_map1.keys():
    if key in c_map2.keys():
      if c_map1[key] != c_map2[key]:
        return False
    else:
      return False
  return True


anagram_val = anagrams("Dormitory", "Dirty room")
print(anagram_val)