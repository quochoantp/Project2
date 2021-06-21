import random as rd
print("Nhap n:")
n = int(input())
file = open("5.2.txt", 'r+')
for i in range(n):
    file.write(str(rd.randint(1, 10000)))
    file.write(" ")
stri = file.read()
print(stri)
list = []
list = stri.split()
print(list)
sum = 0
for i in list:
    sum += int(i)
print("Tong la:", end='')
print(sum)
