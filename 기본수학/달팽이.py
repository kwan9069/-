a,b,v=map(int,input().split())
i=0
l=0
while True:
    i+=a
    l+=1
    if i< v:
        i -= b
    elif i>= v:
        print(l)
        break