def last_digit(n):
    F = [0,1]
    last_digits = [0,1]
    for i in range(2,60):
        F.append(F[i-1]+F[i-2])
        last_digits.append(int(str(F[i])[-1]))
    return last_digits[n % 60]

if __name__ == "__main__":
    print(last_digit(int(input())))
