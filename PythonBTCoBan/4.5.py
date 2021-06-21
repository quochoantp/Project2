import string
print("Nhap chuoi:")
n = str(input())
list = []
list[:0] = n
t = 0
h = 0
s = 0
print(list)
for i in list:
    if str(i).islower() == True:
        t += 1
    if str(i).isupper() == True:
        h += 1
    if str(i).isdigit() == True:
        s += 1
print("So ki tu thuong: ", end='')
print(t)
print("So ki tu hoa: ", end='')
print(h)
print("So ki tu so: ", end='')
print(s)
