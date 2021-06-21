from math import factorial


def com(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))


print("Nhap n:")
n = int(input())
print("Tam giac pascal")
for i in range(0, n+1):
    for j in range(0, n-i+1):
        print("", end=' ')
    for j in range(0, i+1):
        print("{:<3}".format(com(i, j)), end='')
    print("")
