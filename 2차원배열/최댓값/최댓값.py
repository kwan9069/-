import sys
sys.stdin=open('input.txt','rt')
a=[]
for i in range(9):
    x=list(map(int,input().split()))
    a.append(x)
l=0
l2=0
l3=0
for i in range(9):
    for j in range(9):
        if a[i][j] > l:
            l=a[i][j]
            l2=i
            l3=j
print(l)
print(l2+1,l3+1)
