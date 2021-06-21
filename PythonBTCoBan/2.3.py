import array as arr
mang = arr.array('f')
dem = 0
print("Nhap n:")
n = int(input())
for i in range(n):
    mang.append(float(input()))
print("Nhap so thuc x:")
x = float(input())
for j in (mang):
    if x == j:
        ++dem
print("So phan tu co gia tri x la:"+str(dem))
