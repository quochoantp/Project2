import array as arr
mang = arr.array('I')
dem = 0
print("Nhap mang: ")
for i in range(99):
    t = int(input())
    if t == -1:
        break
    else:
        mang.append(t)
        ++dem
print("Mang sau sap xep:")
print(sorted(mang))
