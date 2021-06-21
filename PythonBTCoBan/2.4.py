import array as arr
mang = arr.array('f')
n = int(input())
for i in range(n):
    mang.append(float(input()))
print("Nhap gia tri check x:")
x = float(input())
for j in range(n):
    if x == mang[j]:
        print("Co")
        break
    else:
        print("Khong")
