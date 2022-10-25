a=int(input())
c=[]
for i in range(a):
    b=list(map(int,input().split()))
    c.append(b)
for i in c:
    print(i[0]+i[1])

# print(c[[0]]+c[[1]])
# print(c[[2]]+c[[3]])
# print(c[[4]]+c[[5]])
