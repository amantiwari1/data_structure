class HashTable:
  def __init__(self, size):
    self.data = [None]*size
  
  def _hash(self, key):
    hash = 0
    for i in range(len(key)):
      hash = (hash + ord(key[i]) * i) % len(self.data)
    return hash

  def set(self, key, value):
    address = self._hash(key)
    if (not self.data[address]):
      self.data[address] = [] 
    self.data[address].append([key,value])
  
  def get(self, key):
    address = self._hash(key)
    for items in self.data[address]:
      if items[0] == key:
        return items[1]
    return "Not Found"
    

    
      

hashtable = HashTable(50)

hashtable.set('dad', 45)
hashtable.set('mon', 54)
hashtable.set('sis', 134)
hashtable.set('bro', 4)
print(hashtable.get('sis'))


