def last_digit(n,m):
    remaining = [0,1]
    f = [0,1]
    i = 2
    now = 1
    last = 0
    while(True):
        f.append(f[i-1]+f[i-2])
        r = f[i] % m
        remaining.append(r)
        last = now
        now = r
        i = i + 1 
        if [last, now] == [0,1]:
            break
    return remaining[n % (i-2)]


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(last_digit(a,b))
