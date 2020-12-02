
def selectionSort(arr):
  length = len(arr)
  a = 1
  for i in range(length):
    numofsmall = i
    for j in range(i+1,length):
      if arr[numofsmall] >= arr[j]: 
        numofsmall = j
    temp = arr[i]
    arr[i] = arr[numofsmall]
    arr[numofsmall] = temp

  return arr






arr = [10, 2,1,5,3,4,7]
print(selectionSort(arr))
