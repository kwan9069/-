from collections import Counter
import itertools
x=list(str(input()))
y=0
res={}
for i in x:
    res[i]=x.count(i)
print(res[l])
# for i in range(len(x)):
#
# if x.count('dz=') >= 1 or x.count('c=') >= 1 or x.count('c-')>=1 or x.count('d-')>=1 or x.count('lj')>=1 or x.count('nj')>=1 or x.count('s=')>=1 or x.count('z=') >=1:
#     y+=


for i in range(len(x)):
    if x[i:i+3] == 'dz=':
        y -=1
        continue
    elif x[i:i+2]=='c=' or x[i:i+1]=='c-' or x[i:i+1]=='d-' or  x[i:i+1]=='lj'  or x[i:i+1]=='nj' or x[i:i+1]=='s=' or x[i:i+1]=='z=':
        y -=1
print(y)




