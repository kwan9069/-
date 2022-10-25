x=int(input())
x1=[]
y=list(map(int,input().split()))
y1=max(y)
cnt=0
for i in y:
    x1.append((i/y1)*100)
for l in x1:
    cnt += l
print(cnt/len(x1))
