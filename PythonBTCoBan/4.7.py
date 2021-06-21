def coun(c):
    list = []
    list[:0] = c
    t = 0
    for i in list:
        if str(i).isdigit() == True:
            t += 1
    return t


print("Nhap chuoi:")
n = str(input())
print(coun(n))
