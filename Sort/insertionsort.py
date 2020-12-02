
def insertionSort(arr):
  for i in range(1,len(arr)):
    nextArr = arr[i]
    prevArr = i-1
    while prevArr >= 0 and nextArr < arr[prevArr]:
      arr[prevArr+1] = arr[prevArr]
      prevArr -= 1
    arr[prevArr+1] = nextArr

  return arr

arr = [12, 11, 13, 5, 6]
print(insertionSort(arr))
