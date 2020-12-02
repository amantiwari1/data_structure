
def bubbleSort(arr):
  length = len(arr)
  for c in arr:
    for i in range(length-1):
      if arr[i] > arr[i+1]:
        temp = arr[i]   
        arr[i] = arr[i+1]
        arr[i+1] = temp
    length -= 1
  return arr


arr = [20,3,2,10,1,5]
print(bubbleSort(arr))
