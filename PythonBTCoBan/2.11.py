import random as rd
print("Nhap n:")
list1 = []
n = int(input())
for i in range(n):
    list1.append(rd.randint(1, 100))
print(list1)
list1.reverse()
print(list1)
