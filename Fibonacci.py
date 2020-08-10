import sys
def Fibonacci(n):
    arr = [1,1]
    for i in range(n):
        c = arr[i]+ arr[i+1]
        arr.append(c)
    return arr[n]

if __name__ == "__main__":
    print(Fibonacci((int(input())+1)))
