ex = [1, 2, 3, 4, 5, 6, 7]
for i in ex:
    print(i)
a = [[i]*i for i in ex if i % 2 == 0]
print(a)
