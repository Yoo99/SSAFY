import sys
sys.stdin = open("input.txt")

n = int(input())

sum = 0
cnt = 0
while cnt < n:
    sum +=1
    if "666" in str(sum):cnt +=1
    if cnt == n:
        break
print(sum)
