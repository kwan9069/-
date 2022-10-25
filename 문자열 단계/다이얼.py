x=str(input())
y=[]
for i in x:
    if i == 'A' or i== 'B' or i=='C':
        y.append(3)
    elif i == 'D' or i== 'E' or i=='F':
        y.append(4)
    elif i == 'G' or i== 'H' or i=='I':
        y.append(5)
    elif i == 'J' or i== 'K' or i=='L':
        y.append(6)
    elif i == 'M' or i== 'N' or i=='O':
        y.append(7)
    elif i == 'P' or i== 'Q' or i=='R' or i=='S':
        y.append(8)
    elif i == 'T' or i== 'U' or i=='V':
        y.append(9)
    elif i == 'W' or i== 'X' or i=='Y' or i=='Z':
        y.append(10)
print(sum(y))

