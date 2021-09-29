for i in range(500):
    if i % 7 == 0:
        b = i
        while b > 0:
            a = b % 10
            if a == 8:
                print(i)
                break
            else:
                b = b // 10
