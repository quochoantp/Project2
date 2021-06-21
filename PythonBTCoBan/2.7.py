list = []
print("Nhap n:")
n = int(input())
for i in range(n):
    list.append(int(input()))
print("Nhap x")
x = int(input())
dem = 0
for i in list:
    if i == x:
        list.remove(i)
        dem += 1
print("So phan tu co gia tri x la:")
print(dem)
print(list)
