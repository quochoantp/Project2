print("Nhap chuoi:")
n = str(input())
list = []
list[:0] = n
t = 0
for i in list:
    if i == ' ':
        t += 1
print("So khoang trang:")
print(t)
