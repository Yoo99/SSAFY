import sys
sys.stdin = open("1697_input.txt")

a1,b = map(int,input().split())
dist = abs(a1-b)
cnt = 0
a2 = a1
while a2!=b:
    if a2==b:
        break
    if abs(a2-b)>a1:
        a2  += a1
        cnt +=1
    elif abs(a2-b) <a2:
        if a2<b:
            a2+=1
            cnt+=1
        else:
            a2-=1
            cnt+=1
print(cnt)