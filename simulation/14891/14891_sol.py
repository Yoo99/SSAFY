import sys
sys.stdin = open("input.txt")

chain = []
for _ in range(4):
    line = list(map(int, input()))
    chain.append(line)
n = int(input())# 회전 횟수

for _ in range(n):
    idx, w= map(int,input().split())
    idx -=1
    turn_dir = [0 for _ in range(4)]
    turn_dir[idx] = w
    # 왼쪽에 있는 체인과 비교
    for i in range(idx-1, -1, -1):
        if chain[i][2] == chain[i+1][6]:
            break
        else:
            turn_dir[i] = turn_dir[i+1] * (-1)
    for j in range(idx+1, 4):
        if chain[j-1][2] == chain[j][6]:
            break
        else:
            turn_dir[j] = turn_dir[j-1] * (-1)
    for id in range(4):
        if turn_dir[id] == 0:
            continue
        elif turn_dir[id] == -1: # 반시계 방향
            chain[id] = chain[id][1:] + [chain[id][0]]
        elif turn_dir[id] == 1:# 시계 방향
            chain[id] = [chain[id][-1]] + chain[id][:-1]

answer = 0
if chain[0][0] ==1:
    answer += 1
if chain[1][0] == 1:
    answer += 2
if chain[2][0] == 1:
    answer +=4
if chain[3][0] == 1:
    answer += 8
print(answer)
