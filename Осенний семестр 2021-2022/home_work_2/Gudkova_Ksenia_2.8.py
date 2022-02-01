def more_than_five(lst):
    list1 = []
    for i in lst:
        if i > 10 or i < -10:
            list1.append(i)
    return(list1)


list2 = list(map(int, input().split()))
print(more_than_five(list2))
