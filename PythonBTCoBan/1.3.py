import math
print("Nhap 3 canh:")
a=float(input())
b=float(input())
c=float(input())
if a+b > c and a+c>b and b+c>a:
    print("Day la 1 tam giac")
    d= a+b+c
    print("Chu vi la:")
    print(d)
    p=d/2
    e= math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich la:")
    print(e)
else :
     print("Day khong phai 1 tam giac")