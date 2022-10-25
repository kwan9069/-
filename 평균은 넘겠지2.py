x=int(input())
for _ in range(x):
    y=list(map(int,input().split()))
    cnt=0
    y1=y[1:]
    for l in y1:
        if l > sum(y1)/y[0]:
            cnt += 1
    xf = (cnt / y[0])* 100
    print(f'{xf:.3f}%')
