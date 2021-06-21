file = open("5.1.txt", "r+")
print("Nhap ten nhan vien:")
t = 1
while t != 0:
    n = str(input())
    file.writelines(n)
    file.write(" ")
    if n == "":
        t = 0
stri = file.read()
print(stri)
list = []
list = stri.split()
print(list)
sortlist = []
sortlist = sorted(list)
print(sortlist)
file.close()
