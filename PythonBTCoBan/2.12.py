print("Nhap n:")
n = int(input())
list = []
for j in range(n):
    list.append(int(input()))

i = 0
t = 0
print("Cac day con la:")
while i <= n:
    if list[i] < list[i+1]:
        for k in range(t, i+2):
            print(list[k], end='')
            print(" ", end='')
        print("")
    else:
        t = i+1
    i += 1
