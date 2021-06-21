class Person:
    def __init__(self, ten, birth, sex, address):
        self.ten = ten
        self.birth = birth
        self.sex = sex
        self.address = address

    def showInfo(self):
        print("Thong tin ca nhan:")
        print(self.ten)
        print(self.birth)
        print(self.sex)
        print(self.address)


list = []
for i in range(5):

    print("Nhap thong tin nguoi thu " + str(i+1)+" la:")
    a1 = str(input())
    a2 = str(input())
    a4 = str(input())
    a3 = str(input())
    a = Person(a1, a2, a4, a3)
    list.append(a)
for i in range(5):
    list[i].showInfo()
    print("---------------------")
