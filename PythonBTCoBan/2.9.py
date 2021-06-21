import random as rd
list = []
print("Nhap n:")
n = int(input())
z = 1
for i in range(n):
    y = rd.randint(z, 100+i)
    list.append(y)
    z = y
print(list)
print("Nhap x:")
x = int(input())
j = 0
while j < n:
    if x > list[j]:
        j += 1
    else:
        list.insert(j, x)
        break
print(list)
