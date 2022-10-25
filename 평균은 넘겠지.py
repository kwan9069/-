x=int(input())
for i in range(x):
    y=list(map(int,(input().split())))
    z = []
    for j in range(1,len(y)):
        z.append(y[j])
        x2 = []
    for k in z:
        z1 = sum(z) / len(z)
        if k > z1:
            x2.append(k)
        else:
            continue
    l1 = (len(x2) / len(z))
    l1=float(l1)*100
    print(f'{l1:.3f}', '%')



    #
    #           x2.append(k)
    #         else:
    #             continue
    # print(x2)
    # print(z)
