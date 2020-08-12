def lcm(a,b):
    for i in range(1,(a*b+1)):
        if i % a == 0 and  i % b == 0:
            return i
    return a*b

if __name__ == "__main__":
    a,b = map(int, input().split())
    print(lcm(a,b))
