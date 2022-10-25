x=int(input())
for i in range(1,x+1):
    y=list(map(str,input()))
    tot = 0
    cnt = 0
    for l in y:
        if l == 'O':
            tot+=1
            cnt+=tot
        elif l == 'X':
            tot=0
        else:
            break
    print(cnt)


            # if l=='O':
            #     cnt+=1
            #     tot+=cnt
            #     mak+=1
            #     continue
            # elif l=='X':
            #     cnt=0
            #     mak+=1
            #     continue
            # elif mak==len(x):
            #     print(tot)
            #     break




