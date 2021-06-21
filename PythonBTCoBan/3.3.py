print("Nhap n:")
n = int(input())
list = []
list1 = []
for i in range(n):
    list.append(int(input()))
    if list[i] % 2 == 0:
        list1.append(list[i])
sum = 0
for j in range(len(list1)):
    sum += list1[j]
print("Trung binh day la:", end='')
print(sum/len(list1))
