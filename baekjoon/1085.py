x, y, w, h = map(int, input().split())
if (w/2 > x and h/2 > y):
    if x >= y:
        print(y)
    elif x < y:
        print(x)
elif (w/2 < x and h/2 < y):
    if x >= y:
        print(w-x)
    elif x < y:
        print(h-y)
elif (w/2 < x and h/2 > y):
    if x >= h-y:
        print(h-y)
    elif x < h-y:
        print(h-y)
elif (w/2 > x and h/2 < y):
    if w-x >= y:
        print(y)
    elif w-x < y:
        print(w-x)




