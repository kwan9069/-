x=int(input())
for i in range(x):
    j=list(map(int,input().split()))
    for l in range(i+1,i+2):
        print('Case', f'#{l}:',j[0],'+',j[1],'=',j[0]+j[1])