import sys
sys.stdin = open("input.txt")

from collections import defaultdict

n = int(input())
ans =[]
cnt = defaultdict(int)
arr = list(map(int, input().split()))
for ele in arr:
    cnt[ele]+=1
max_count = max(cnt.values())
for key in cnt.keys():
    if cnt[key]==max_count:
        ans.append(key)
ans.sort()
answer = ''
for d in ans:
    answer += str(d) + " "
print(answer.rstrip())
