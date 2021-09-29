x = [input() for i in range(10)]
l = len(x)
b = ['' for i in range(l)]
ind = 0
for i in x:
    if ind % 2 == 0:
        b[ind] = i
    else:
        ind1 = l - ind
        b[ind1] = i
    ind += 1
print(b)
