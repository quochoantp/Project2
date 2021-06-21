import random
a = float(input())
b = float(input())
c = float(input())
d = random.randint(1, 100000)
print(d)
if a > b:
    e = a
else:
    e = b
if c > e:
    e = c
if d > e:
    e = d
print("So lon nhat la:")
print(e)
