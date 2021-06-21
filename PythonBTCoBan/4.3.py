dic = {1: 'mot', 2: 'hai', 3: 'ba', 4: 'bon', 5: 'nam',
       6: 'sau', 7: 'bay', 8: 'tam', 9: 'chin', 0: 'khong'}
dic1 = {1: '', 2: 'nghin', 3: 'trieu', 4: 'ti', 5: 'nghin ti'}
dic2 = {1: '', 2: 'muoi', 3: 'tram'}
print("Nhap so can doc:")
n = int(input())
list = []
list1 = []
t = 0
while n != 0:
    list.append(int(n % 1000))
    n = int(n/1000)
print(list)
for i in list:
    t += 1
    u = 0
    list1.append(dic1[t])
    while i != 0:
        u += 1
        list1.append(dic2[u])
        list1.append(dic[int(i % 10)])
        i = int(i / 10)

for item in reversed(list1):
    print(item, end=' ')
