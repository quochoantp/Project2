print("Nhap n:")
n = int(input())
list = []
m = int(n/2)
for i in range(n):
    list.append(int(input()))
j = 0
for j in range(0, m):
    if list[j] == list[n-1-j]:
        continue
    else:
        print("Day khong doi xung")
        exit()
print("Day doi xung!")
