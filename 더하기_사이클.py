tot = 0
x = list(str(input()))
l = x[0]+ x[1]
l= int(l)
while True:
    for i in x:
        cnt=0
        cnt+=int(i)
        x=x[1]+str(cnt%10)
        if l!= int(x):
            tot+=1
            x = list(str(x))
            continue
        elif l==int(x):
            break
print(tot)
# if int(x) < 10





