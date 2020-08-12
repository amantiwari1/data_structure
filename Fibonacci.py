# Uses python3
def calc_fib(n):
    if 1 >= n:
        return n
    arr = [0,1]
    for i in range(1,n):
        a = arr[0] + arr[1]
        arr[0] = arr[1]
        arr[1] = a
    return arr[1]


n = int(input())
print(calc_fib(n))
