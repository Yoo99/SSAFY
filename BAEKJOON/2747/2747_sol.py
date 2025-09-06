import sys
sys.stdin = open("input.txt")

fibo=[0, 1]
total ,cnt = 0, 0
n = int(input())
while cnt < n:
    cnt +=1
    total = fibo[cnt-1] + fibo[cnt]
    fibo.append(total)
    if cnt == n:
        break
print(fibo[cnt])