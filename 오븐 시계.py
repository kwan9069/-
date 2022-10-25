A,B=map(int,input().split())
C=int(input())
E=int((B+C)%60)
D=int((B+C)//60)
if Q <= 23 :
    if B+C >= 60 and C >= 60 and C+D >= 60:
        print(A+E+1,(B+C)-(60*(E+1)),sep=' ')
    elif B+C >= 60 and C >= 60:
        print(A+E,D,sep=' ')
    elif B+C >= 60 and B <= 60 and C <=60:
        print(A+1,B+C-60)
    elif B+C < 60:
        print(A,B+C,sep=' ')
elif Q > 24:
    if B+ C >= 60 :
        print(A+E-24, B + C - (60 * E),sep=' ')








