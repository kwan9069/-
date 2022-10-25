t=int(input)
for i in t:
    k=str(input())
    n=str(input())
    c=0
    d=0
    for i in range(0,k):
        for j in range(0,n):
            if i==0:
                c+=j
            else:
                d+=c



            #  1층  3호는 0층에서 3호까지 (3+2+1)
        # 2층 3호는 1층에서 3호까지- 1층 1호에서 3호까지 (6+3+1)  3층 3호는 2층 1호에서 3호까지 (10+9+4)

