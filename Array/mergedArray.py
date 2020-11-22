def mergedSortArray(arr1, arr2):
  mergedSortArray1=[]
  arr1Item = arr1[0]
  arr2Item = arr2[0]
  i = 1
  j = 1
  arr1len= len(arr1)
  arr2len= len(arr2)

  while(arr1Item or arr2Item):
    if arr1Item != None and arr1Item < arr2Item:
      mergedSortArray1.append(arr1Item)
      if arr1len == i:
        arr1Item = None
      else:
        arr1Item = arr1[i]
        i += 1
    else:
      mergedSortArray1.append(arr2Item)
      if arr2len == j:
        arr2Item = None
      else:
        arr2Item = arr2[j]
        j += 1

  return mergedSortArray1


def main():
  arr1 = [0,3,4,5]
  arr2 = [4,6,30, 54]
  print(mergedSortArray(arr1, arr2))


if __name__ == "__main__":
  main()
