x,y=map(int,input().split())
b=[]
if x/2==1:
    b.append(31)
elif x/3==1:
    b.append(31*1+28)
elif x/4==1:
    b.append(31*2+28)
elif x/5==1:
    b.append(31*2+28+30)
elif x/6==1:
    b.append(31*3+28+30*1)
elif x/7==1:
    b.append(31*3+28+30*2)
elif x/8==1:
    b.append(31*4+28+30*2)
elif x/9==1:
    b.append(31*5+28+30*2)
elif x/10==1:
    b.append(31*5+28+30*3)
elif x/11==1:
    b.append(31*6+28+30*3)
elif x/12==1:
    b.append(31*6+28+30*4)
b.append(y)
result=0
for i in b:
    result+=int(i)
if result%7==0:
    print('SUN')
elif result%7==1:
    print('MON')
elif result%7==2:
    print('TUE')
elif result%7==3:
    print('WED')
elif result%7==4:
    print('THU')
elif result%7==5:
    print('FRI')
elif result%7==6:
    print('SAT')
