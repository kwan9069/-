import sys
sys.stdin=open('input.txt','rt')
n=int(input())
m=list(map(int,input().split()))
v=int(input())
cnt=0
for i in m:
    if i==v:
        cnt+=1
print(cnt)