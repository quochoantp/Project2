list = []
n = int(input())
for i in range(n):
    list.append(int(input()))
print("Nhap x,k:")
x = int(input())
k = int(input())
list.insert(k, x)
print(list)
