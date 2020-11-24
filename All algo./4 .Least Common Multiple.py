def GCD(a, b):
    if b == 0:
        return a
    else:
         r = a % b
         return GCD(b, r)

def LCM(a, b):
    return int(a * b / GCD(a, b))

if __name__ == "__main__":
    a,b = map(int, input().split())
    print(LCM(a,b))
