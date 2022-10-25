from collections import Counter
import itertools
x=list(str(input().lower()))

res={}
for i in x:
    res[i]=x.count(i)

l1=[(k, len(list(v))) for k, v in itertools.groupby(sorted(res.values()))]
l2=max(l1)
if l2[1]>1:
    print('?')
c=Counter(res)
print(dict(res.items()))
print(res)
print(max(res.values()))
# x=list(str(input()))
# y=[]
# y1=[]
# y2=[]
# y3=[]
# y5=[]
# for i in x:
#     if len(x)==1:
#         print(i.upper())
#     else:
#         i=i.lower()
#         l=ord(i)
#         y3.append(l)
# if len(y3)>=1:
#     for j in y3:
#         if j==max(y3):
#             y.append(j)
#         else:
#             y1.append(j)
#     for i in y1:
#         a=y1.count(i)
#         y2.append(a)
#     b=y.count(y[0])
#     if b==max(y2):
#             print('?')
#     else:
#         y4=max(y3,key=y3.count)
#         print(chr(y4).upper())

