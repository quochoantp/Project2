import array as arr
t = 0
max = 0

mang = arr.array('i')
for x in range(99):
    i = int(input())
    if i == -1:
        break
    t += 1
    mang.append(i)


for y in range(t):
    print(str(y) + ":"+str(mang[y]))
    if max > mang[y]:
        max = max
    else:
        max = mang[y]
print(t)
print("Max la: " + str(mang[y]))
