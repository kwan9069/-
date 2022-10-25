x=list(map(int,input().split()))
y=[]
y1=[]
for i in x:
    y.append(str(i)[::-1])
for i in y:
    y1.append(int(i))
print(max(y1))
