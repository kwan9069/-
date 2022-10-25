x=list(map(int,input().split()))
y=list(map(int,input().split()))
for i in y:
    if i < x[1]:
        print(i,end=' ')