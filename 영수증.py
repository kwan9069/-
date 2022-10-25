a=int(input())
b= int(input())
e=[]
for i in range(1,b+1):
    c,d=map(int,input().split())
    e.append(c*d)
i = 0
cnt=0
while i <= (len(e)-1):
    cnt += e[i]
    i += 1
if cnt == a:
    print('Yes')
else:
    print('No')