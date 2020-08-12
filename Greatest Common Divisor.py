def gcd(a,b):
    c = 1
    for i in range(2,min(a,b)+1):
        if a % i == 0 and b % i == 0:
            if  i > c:
                c = i
    return c

if __name__ == '__main__':
    a,b = map(int, input().split())
    print(gcd(a,b))
