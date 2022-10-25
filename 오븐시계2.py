A,B=map(int,input().split())
C=int(input())
D=int((B+C)%60)
E=int((B+C)//60)
if A+E < 24:
    print(A+E,D,sep=' ')
elif A+E >= 24:
    print(A+E-24,D,sep=' ')
