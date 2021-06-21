print("Nhap n:")
n = int(input())
list = []
list1 = []
while n > 99 or n <= 0:
    print("Vui long nhap lai 0<n<99 :")
    n = int(input())
print("Nhap k:")
k = int(input())
for i in range(n):
    list.append(int(input()))
    list1.append(0)
for i in range(k, n):
    list1[i-k] = list[i]
for i in range(0, k):
    list1[n-k+i] = list[i]
print("Day sau khi xoay vong " + str(k)+" lan la:")
print(list1)
