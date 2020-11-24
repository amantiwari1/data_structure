# class HighestNumber:
#   def __init__(self, array1):
#     self.data = [None]*(max(array1)+1)
#     self.size = len(array1)
#     for i in array1:
#       self.set(i,i)

#   def set(self, key,value):
#     if (not self.data[key]):
#       self.data[key] = [key, 0]
#     a = self.data[key][1]+1
#     self.data[key][1] = a
  
#   def get(self, key):
#     return self.data[key] 

#   def answer(self):
#     a = 1
#     j = 0
#     for i in self.keys():
#       if a < i[1]:
#         a,j = i[1],i[0]
#     if a == 1:
#       return "None"
#     else:
#       return j
      
      

#   def keys(self):
#     array_keys = []
#     for i in self.data:
#       if i:
#         array_keys.append(i)
#     return array_keys


def firstRecurring(arr1):
  map = {}
  for i in arr1:
    if map.get(i):
      map[i] += 1
    else:
      map[i] = 1 
  for j in map: 
    if map[j] > 1:
      return j
  return None

def main():
  print(firstRecurring( [1,2,5,5,2,4]))

main()