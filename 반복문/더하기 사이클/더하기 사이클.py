import sys
sys.stdin=open('input.txt','rt')
x=int(input())
num=x
cnt=0
while True:
    y=x//10
    y1=x%10
    y2=y+y1
    y=str(y1)+str(y2%10)
    y=int(y)
    x=y
    cnt+=1
    if num==y:
        break
print(cnt)
