print("Nhap chuoi,n,k:")
s = str(input())
n = int(input())
k = int(input())
list = []
list[:0] = s
for i in range(k, (k+n)):
    list.remove(list[i])
print(list)
