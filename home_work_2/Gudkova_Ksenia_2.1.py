def distance(x1, y1, x2, y2):
    dy = (y1 - y2) * (y1 - y2)
    dx = (x1 - x2) * (x1 - x2)
    s = (dy + dx)**0.5
    return(s)


x1, y1, x2, y2 = map(int, input().split())
print(distance(x1, y1, x2, y2))
