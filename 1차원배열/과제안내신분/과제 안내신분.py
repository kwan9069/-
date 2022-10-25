import sys
sys.stdin=open('input.txt','rt')
l=[]
for i in range(28):
    n=int(input())
    l.append(n)
l2=list(range(1,31))
for i in l2:
    if i not in l:
        print(i)

