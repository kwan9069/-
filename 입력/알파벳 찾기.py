import string
x=str(input())
lower=[i for i in string.ascii_lowercase]
for i in lower:
    if i not in x:
        print(-1)
    if i in x:
        print(x.index(i),end=' ')
