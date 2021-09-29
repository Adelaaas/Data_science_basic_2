for i in range(500):
    if i % 7 == 0 and i < 10:
        if i % 10 == 8:
            print(i, end=' ')
    if i % 7 == 0 and i > 10 and i < 100:
        if i % 10 == 8 or (i // 10) % 10 == 8:
            print(i, end=' ')
    if i % 7 and i > 100:
        if i % 10 == 8 or (i // 10) % 10 == 8 or (i // 100) % 10 == 8:
            print(i, end=' ')
