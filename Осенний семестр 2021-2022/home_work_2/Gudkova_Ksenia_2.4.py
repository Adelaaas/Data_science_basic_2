def reverse_list(lst):
    list2 = []
    for i in range(len(lst) - 1, -1, -1):
        list2.append(lst[i])
    return(list2)


list1 = list(map(int, input().split()))
print(reverse_list(list1))
