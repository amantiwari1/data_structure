class Stack:
  def __init__(self):
    self.top = None
    self.buttom = None
    self.length = 0

  def nodes(self, value):
    return {"value":value, "next":None}
  

  def peek(self):
    return "Top : "+ str(self.top["value"])


  def push(self, value):
    newNodes = self.nodes(value)
    if self.buttom is None:
      self.buttom = newNodes
      self.top = newNodes
    else:
      hold = self.top
      self.top = newNodes
      self.top["next"] = hold    
    self.length += 1

  def get(self):
    arr = []
    nex = self.top
    for i in range(self.length):
      val = nex["value"]
      arr.append(val)
      nex = nex["next"]
    return arr

  def pop(self):
    if self.top == self.buttom:
      self.buttom = None 
    self.top = self.top["next"]
    self.length -= 1

# class Node():
#   def __init__(self,value):
#     self.value = value
#     self.next = None

  

stack = Stack()

stack.push(1)
stack.push(2)
print(stack.peek())
stack.pop()
print(stack.top)
print(stack.get())

