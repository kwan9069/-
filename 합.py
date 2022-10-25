a=int(input())
i=0
cnt=0
while i < a:
    i += 1
    cnt += i
    if i >= a:
        break
print(cnt)