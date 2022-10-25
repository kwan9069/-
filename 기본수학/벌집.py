x=int(input())
y = 1
y2= 1
y1 = 1
while True:
    y1 += 6*y
    y2 += 6* (y-1)
    if x >= y1:
        y += 1
    elif y1 >x and y2 < x:
        y += 1
        print(y)
        break
    elif y1 > x:
        print(y)
        break



