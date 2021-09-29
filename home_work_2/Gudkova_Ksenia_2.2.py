def season(month):
    global s
    if month > 0 and month < 3 or month == 12:
        s = 'зима'
    elif month >= 3 and month <= 5:
        s = 'весна'
    elif month >= 6 and month <= 8:
        s = 'лето'
    else:
        s = 'осень'
    return None


month = int(input())
season(month)
print(s)
