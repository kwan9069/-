x=int(input())
result=0
for i in range(x):
    y=list(map(int,input().split()))
    for l in range(i+1,i+2):
        print('Case',f'#{l}:',y[0]+y[1])