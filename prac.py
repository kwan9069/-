l1=[]
for i in range(1,11):
    x=int(input())
    l=x%42
    l1.append(l)
l2=[]
cnt=0
for i in l1:
    if i not in l2:
        l2.append(i)
print(len(l2))
