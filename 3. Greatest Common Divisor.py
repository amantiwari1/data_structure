def gcd(a,b):
    if b == 0:
        return a
    else:
        z = a % b
        return gcd(b,z)

if __name__ == '__main__':
    a,b = map(int, input().split())
    print(gcd(a,b))
