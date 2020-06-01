def pyramid(n):
  total_width = 2*n-1
  mid_point = int(total_width / 2) 
  for row in range(n):
    string = ""
    for cell in range(total_width):
      if cell >= mid_point - row and cell <= mid_point + row:
          string += "x"
      else:
          string += "."
    print(string)
      
#pyramid(4)

def rec_pyramid(n, row = 0, string=""):
  if row == n:
    return ;
  
  total_width = 2*n - 1
  mid_point = int(total_width/2)
  if len(string) == total_width:
    print(string)
    return rec_pyramid(n, row + 1, "")

  if len(string) >= mid_point - row and len(string) <= mid_point + row:
    string += "x"
  else:
    string += "."
  return rec_pyramid(n, row, string)
  
 
  
rec_pyramid(2, 0)

def print_pyramid(n, row):
  if row == n:
    return
  
  total_width = int(2*n-1)
  mid_point = int(total_width/2)
  number_of_x = 2*(row+1) - 1
  half_number_of_spaces = int((total_width - number_of_x)/2)

  string = ""

  for i in range(total_width):
    if i >= half_number_of_spaces and i < number_of_x + half_number_of_spaces: 
      string += "x"
    else:
      string += "."

  print(string)
  return print_pyramid(n, row + 1)


  

print_pyramid(2, 0)