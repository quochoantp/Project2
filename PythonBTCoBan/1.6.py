
print("Nhap a,b:")
a=float(input())
b=float(input())
print("Nhap dau:")
c= input()
if c==">":
    if a==0:
        if b>0: print("Phuong trinh vo so nghiem!")
        else: print("Phuong trinh vo nghiem")
    else:
        d= -b/a
        print("Phuong trinh co nghiem nam trong khoang: (" + str(d)+ ", +oo)")
else:
     if a==0:
        if b<0: print("Phuong trinh vo so nghiem!")
        else: print("Phuong trinh vo nghiem")
     else:
        e= -b/a
        print("Phuong trinh co nghiem nam trong khoang: (-00, " + str(e)+ ")")
