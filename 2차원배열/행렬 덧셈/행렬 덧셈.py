import sys
sys.stdin=open('input.txt','rt')
# n,m=map(int,input().split())
# x=[n*[0]]*m
# x1=[n*[0]]*m
# for i in range(1):
#     for j in range(m):
#         a,b,c=map(int,input().split())
#         x[j]=[a,b,c]
# for i in range(1):
#     for j in range(m):
#         e,f,g=map(int,input().split())
#         x1[j]=[e,f,g]
# for i in range(n):
#     for j in range(m):
#         print(x[i][j]+x1[i][j],end=' ')
#     print()

A,B=[],[]
n,m=map(int,input().split())
for i in range(n):
    i=list(map(int,input().split()))
    A.append(i)
for i in range(m):
    i=list(map(int,input().split()))
    B.append(i)
for i in range(n):
    for j in range(m):
        print(A[i][j]+B[i][j],end=' ')
    print()