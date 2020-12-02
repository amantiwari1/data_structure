def mergeSort(arr):
  if len(arr) == 1:
      return arr
  
  length = len(arr)
  half = length//2
  left, right = arr[:half],arr[half:]
  
  return merge(
    mergeSort(left),
    mergeSort(right)
  )

def merge(left, right):
  result = []
  leftIndex = 0
  rightIndex = 0
  while leftIndex < len(left) and  rightIndex < len(right):
    if left[leftIndex] < right[rightIndex]:
      result.append(left[leftIndex])
      leftIndex += 1
    else:
      result.append(right[rightIndex])
      rightIndex += 1
  result.extend(left[leftIndex:])
  result.extend(right[rightIndex:])
  return result

print(mergeSort([8,9,5,7,3,2,4,6]))