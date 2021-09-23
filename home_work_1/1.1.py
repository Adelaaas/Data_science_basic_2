listpart1 = [1, 2, 3, 4, 5, 6, 7]
i = int(input())
print(i)
listpart2 = []
for i in listpart1:
    if i % 2 == 0:
        listpart2.append([i]*i)
print(listpart2)
