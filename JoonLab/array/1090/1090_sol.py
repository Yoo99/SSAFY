import sys
sys.stdin = open("input.txt")

answer = 0
arr =list(map(str, input().split()))
key = str(input())
for ele in arr:
    if key in ele and key!=ele:
        answer +=1
    else:
        continue
print(answer)