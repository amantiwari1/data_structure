class LinkedList:
  def __init__(self, value):
    self.head = self.Node(value)
    self.tail = self.head
    self.length = 1;

  def Node(self, value):
    return {"value": value, "next":None}
  
  
  def get(self):
    arr = []
    currentNodes = self.head
    while currentNodes["next"] != None:
      arr.append(currentNodes["value"])
      currentNodes = currentNodes["next"]
    arr.append(currentNodes["value"])
    return arr
      
  
  def append(self, value):
    newNodes = self.Node(value)
    self.tail["next"] = newNodes
    self.tail = newNodes
    self.length += 1

  def prepend(self, value):
    newNodes = self.Node(value)
    newNodes['next'] = self.head
    self.head = newNodes
    self.length += 1   

  def insert(self, index, value):
    if index == 0:
      return self.prepend(value)
    elif index >= self.length:
      return self.append(value)
    pre = self.head
    for i in range(1,index):
      pre = pre["next"]
    aft = pre["next"]
    newNodes = self.Node(value)
    newNodes["next"] = aft
    pre["next"] = newNodes
    self.length += 1

  def delete(self, index):
    pre = self.head
    for i in range(1,index):
      pre = pre["next"]
    unwantedNodes = pre["next"]
    aft = unwantedNodes["next"]
    pre["next"] = aft
    del unwantedNodes
    self.length += 1




linked = LinkedList(10)
linked.append(5)
linked.append(16) 
linked.append(14) 
linked.append(14) 
linked.append(13) 
linked.prepend(1)
linked.prepend(3) 
linked.insert(12,99)
linked.insert(0,9)
linked.insert(5,55)
linked.delete(5)
print(linked.get())
linked.delete(6)
print(linked.get())