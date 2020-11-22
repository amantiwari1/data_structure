class MyArray:
  global data
  global length
  data = {}
  length = 0

  def get_data():
    return data

  def get(index):
    return data[index]
  
  def push(item):
    global length
    data[length] = item
    length = length + 1
  
  def pop():
    global length
    del data[length-1]
    length = length-1
  
  def delete(index):
    global length
    del data[index]
    length = length-1


def main():
    array = MyArray()
    MyArray.push(1)
    MyArray.push(2)
    MyArray.delete(0)
    print(MyArray.get_data())

if __name__ == "__main__":
  main()


