x=int(input())
z=0
for i in range(1,x+1):
    y=list(map(str,input()))
    for i in y:
        if y[i+1]==y[i]:
            z+=1

