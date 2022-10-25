x=[]
x2=[]
def d():
    for i in range(1,10001):
            n = i%10+(i%100//10)+(i%1000//100)+(i//1000)+i
            if n < 10000:
                x.append(n)
    for l in range(1,10000):
        if l not in x:
            print(l)
d()