import json

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def node(self, value):
    return {
      "value": value,
      "left" : None,
      "right": None 
    }

  def insert(self, value):
    newNodes = self.node(value)
    if self.root is None:
      self.root = newNodes 
    else:
      currentNodes = self.root
      while 1:
        if value < currentNodes["value"]:
          if not currentNodes["left"]:
            currentNodes["left"] = newNodes
            return None
          currentNodes = currentNodes["left"]
        else:
          if not currentNodes["right"]:
            currentNodes["right"] = newNodes
            return None
          currentNodes = currentNodes["right"]
      
  def lookup(self, value):
    currentNodes = self.root
    while currentNodes:
      if value < currentNodes["value"]:
        currentNodes = currentNodes["left"]
      elif value > currentNodes["value"]:
        currentNodes=currentNodes["right"]
      elif value == currentNodes["value"]:
        return currentNodes

    return None

  def get(self):
    return json.dumps(self.root, indent=2)

  def BFS(self):
    currentNodes = self.root
    lists= []
    queue = []
    queue.append(currentNodes)
    while len(queue) > 0:
      currentNodes = queue[0]
      del queue[0]
      lists.append(currentNodes['value'])
      if currentNodes['left']:
        queue.append(currentNodes['left'])  
      if currentNodes['right']:
        queue.append(currentNodes['right'])  

    return lists

  def DFSInOrder(self):
    return self.TraverseInOrder(self.root, [])

  def DFSPreOrder(self):
    return self.TraversePreOrder(self.root, [])

  def DFSPostOrder(self):
    return self.TraversePostOrder(self.root, [])

  def TraverseInOrder(self,nodes, lists):
    if nodes['left']:
      self.TraverseInOrder(nodes['left'], lists)

    lists.append(nodes['value'])

    if nodes['right']:
      self.TraverseInOrder(nodes['right'], lists)
    
    return lists

  def TraversePreOrder(self,nodes, lists):
    lists.append(nodes['value'])
    
    if nodes['left']:
      self.TraversePreOrder(nodes['left'], lists)


    if nodes['right']:
      self.TraversePreOrder(nodes['right'], lists)
    
    return lists

  def TraversePostOrder(self,nodes, lists):
    if nodes['left']:
      self.TraversePostOrder(nodes['left'], lists)


    if nodes['right']:
      self.TraversePostOrder(nodes['right'], lists)
    lists.append(nodes['value'])
    
    return lists

tree = BinarySearchTree()

tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

print(tree.DFSInOrder())
print(tree.DFSPreOrder())
print(tree.DFSPostOrder())