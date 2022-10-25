n=int(input())
a = []
def han(n):
    global a
    for i in range (1,n+1):
        x=i//100
        x1=(i%100)//10
        x2=i%10
        if i < 100:
            a.append(i)
        elif x1-x== x2-x1:
            a.append(i)
    return len(a)
result=han(n)
print(result)
