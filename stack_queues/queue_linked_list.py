class QueueLinkedList:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def nodes(self, value):
    return {"value":value, "next": None}

  def enqueue(self, value):
    newNodes = self.nodes(value)
    if self.last is None:
      self.first = newNodes
      self.last = newNodes
    else:
      self.last["next"] = newNodes
      self.last = newNodes
      
    self.length+=1

  def dequeue(self, value):
    pass

queue = QueueLinkedList()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.first)
print(queue.last)
    