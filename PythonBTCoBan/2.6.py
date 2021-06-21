list = []
print("Nhap n:")
n = int(input())
for i in range(n):
    list.append(int(input()))
print("Nhap k:")
k = int(input())
if k >= n:
    print("k khong hop le")
else:
    list.remove(list[k-1])
print(list)
