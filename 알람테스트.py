A,B=map(int,input().split())
if B >= 45:
    print(A,B-45,sep=' ')
elif B <= 45 and A== 0:
    print(23,B+60-45,sep=' ')
else:
    print(A - 1, B + 60 - 45, sep=' ')