def quickSort(arr):
  if len(arr) <= 1:
    return arr
  lower = []
  upper = []
  key = arr.pop()
  for i in arr: 
    if key > i:
      lower.append(i)
    else:
      upper.append(i)
  
  return quickSort(lower) + [key] + quickSort(upper)





arr = [0,9,3,8,2,7,5]
print(quickSort(arr))


