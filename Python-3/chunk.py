# array chunking
def get_slice(array, start_index, stop_index):
  # chunk = array[start_index:stop_index]
  # for i in chunk:
  #     array.remove(i)
  # return array, chunk
  chunk = []
  for i in range(start_index, stop_index):
    if i + 1 >= len(array):
      chunk.append(array.pop(i))
  return array, chunk



def chunk(array, chunk_size):
  list_of_chunks = []

  if len(array) <= chunk_size:
     list_of_chunks.append(array)
  else:
    start_index = 0
    while len(array) > 0:
      
      # chunk = []
      # for i in range(start_index, chunk_size):
      #   if i < len(array) - 1:
      #     chunk.append(array.pop(i))

      
      array, chunk = get_slice(array, 0, chunk_size)
      list_of_chunks.append(chunk)
  
  return list_of_chunks

print(chunk([1,2,3,4,5,6], 5))
# [[1, 2, 3, 4, 5], [6]]