print("Nhap n(0<n<=9):")
n = int(input())
while (n > 9) or (n < 0):
    print("Nhap lai n:")
    n = int(input())
list = []
list1 = []
list2 = []
for i in range(n):
    list.append(int(input()))
    if list[i] % 2 == 0:
        list1.append(list[i])
    else:
        list2.append(list[i])
print("Mang chua so chan:")
print(list1)
print("Mang chua so le:")
print(list2)
