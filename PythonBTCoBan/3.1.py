print("Nhap n:")
n = int(input())
list = []
for i in range(n):
    list.append(int(input()))
print("Nhap k:")
k = int(input())
list1 = sorted(list)
print("Phan tu lon thu k trong mang: ", end='')
print(list1[k-1])
