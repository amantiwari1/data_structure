# // method 1
def reverse(string):
  saved_array = []
  for i in string:
    saved_array.insert(0,i)
  return "".join(saved_array)

# // method 2
def reverse1(string):
  return string[::-1]

# // method 3
def reverse2(s):
  string = ""
  for i in s:
    string =  i + string
  return string

# // method 4
def reverse3(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse3(s[1:]) + s[0] 

# // method 5
def reverse4(string): 
    string = "".join(reversed(string)) 
    return string 

