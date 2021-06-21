import random as rd
list1 = []
list2 = []
print("Nhap n:")
n = int(input())
for i in range(n):
    list1.append(rd.randint(1, 100))
print(list1)
print("Nhap x:")
x = int(input())
for j in list1:
    if(j <= x):
        list2.append(j)
print("Day nho hon hoac bang x la:")
print(list2)
