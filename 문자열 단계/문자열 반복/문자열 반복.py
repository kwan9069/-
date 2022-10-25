T=int(input())
b=[]
c=[]
for i in (1,T+1):
    x=list(map(str, input().split()))
    b.append(x)
for i in b:
    for l in i:
        c.append(l)
for i in range(1,len(c),2):
    for l in c[i]:
        print(l*(int(c[i-1])),end='')
    print()





