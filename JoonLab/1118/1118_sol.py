import sys
sys.stdin = open("input.txt")

n = int(input())
sum = 0
while n>=1:
    if n ==1:
        sum +=n
        break
    sum +=n
    n-=1
print(sum)