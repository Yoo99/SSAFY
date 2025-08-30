import sys
sys.stdin = open("input.txt")

M = int(input())
# 전체 숫자의 길이
answer  = 0
for i in range(1, M):
    total = 0
    total += i
    sub = list(str(i))
    for ele in sub:
        total += int(ele)
    if total == M:
        answer = i
        break
print(answer)