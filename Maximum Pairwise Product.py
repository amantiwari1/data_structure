def  max_pro(n,numbers):
    max_index=-1
    for i in range(n):
        if max_index == -1 or numbers[i] > numbers[max_index]:
            max_index = i

    max_index1 = -1
    for i in range(n):
        if i != max_index and ( max_index1 == -1 or numbers[i] > numbers[max_index1] ):
            max_index1 = i
    return numbers[max_index] * numbers[max_index1]

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    print(max_pro(n,numbers))
