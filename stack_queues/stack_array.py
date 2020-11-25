class MyStackArrays:
  def __init__(self):
    self.arrays = []

  def peek(self):
    return self.arrays[0]

  def push(self, value):
    if self.arrays is None:
      self.arrays = []
    self.arrays.insert(0,value)
  
  def pop(self):
    del self.arrays[0]

  def get_data(self):
    return self.arrays



stack = MyStackArrays()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
print(stack.peek())
print(stack.get_data())

  
