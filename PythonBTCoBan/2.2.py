import array as arr
mang = arr.array('i')
print("Nhap n:")
t = 0
n = int(input())
for x in range(n):
    mang.append(int(input()))
    t += mang[x]
td = t/n
print("Gia tri trung binh la:" + str(td))
