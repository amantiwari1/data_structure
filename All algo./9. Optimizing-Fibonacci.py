class fib:
  def __init__(self):
    self.cache = {}
    
  def fib1(self,n):
    if (n-1) in self.cache:
      return "Found in cache : "+str(self.cache.get(n-1))
    else:
      arr = [0,1]
      for i in range(n):
        arr[0], arr[1] = arr[1], arr[0]+arr[1]
        self.cache[i] = arr[0] 

    return arr[0]

optimized_fib = fib()

print(optimized_fib.fib1(1))
print(optimized_fib.fib1(2))
print(optimized_fib.fib1(2))
print(optimized_fib.fib1(2))
print(optimized_fib.fib1(20))
print(optimized_fib.fib1(15))