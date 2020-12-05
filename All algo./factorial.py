def factorial(num):
  if num <= 1:
    return 1
  return factorial(num-1) * num

def fibonacci(num):
  if num == 0:
    return 0
  elif num <= 2:
    return 1
  
  return fibonacci(num-1) + fibonacci(num-2)


  


print(fibonacci(8))