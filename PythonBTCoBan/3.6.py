print("Nhap n:")
n = int(input())
list = []
while n > 20:
    print("Nhap sai.Nhap lai!")
    n = int(input())
for i in range(n):
    m = int(input())
    while m < 0 and m > 10:
        print("Nhap lai:")
        m = int(input())
    list.append(m)
list1 = []
new = []
for i in range(11):
    list1.append(0)
for i in range(n):
    list1[list[i]] += 1
max = 0
for i in range(11):
    if list1[max] < list1[i]:
        max = i
print("So xuat hien nhieu nhat la: ", end=' ')
print(max)
