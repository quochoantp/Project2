print("Nhap chuoi 1:")
a = str(input())
list1 = []
list1 = a.split()
print("Nhap chuoi 2:")
b = str(input())
list2 = []
list2 = b.split()
for i in list1:
    for j in list2:
        if j == i:
            list1.remove(i)
print(list1)
stri = ''
print(stri.join(list1))
