import sys
sys.stdin = open("input.txt")

N = int(input())
people = []
result = []
for _ in range(N):
    x,y = map(int, input().split())
    people.append([x,y])

for idx in range(N):
    cnt = 1
    w1, h1 = people[idx]
    for ele in range(0, N):
        if ele == idx:
            continue
        w2, h2 = people[ele]
        if w1<w2 and h1<h2:
            cnt +=1
    result.append(cnt)
print(*result)