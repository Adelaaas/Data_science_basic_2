def more_than_five(lst):
    b = []
    for i in lst:
        if abs(i) > 10:
            b += [i]
    print(b)

