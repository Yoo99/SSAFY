import sys
sys.stdin = open("input.txt")

def check(maze):
    answer = 0
    # 열 확인
    for idx in range(5):
        total = 0
        for idy in range(5):
            total += maze[idy][idx]
        if total == 0:
            answer += 1
    # 행 확인
    for idx in range(5):
        total = 0
        for idy in range(5):
            total += maze[idx][idy]
        if total == 0:
            answer += 1

    # 대각선 줄 확인
    total1, total2 = 0,0
    for idx in range(5):
        total1 += maze[idx][idx]
    if total1 == 0:
        answer += 1
    for idx in range(5):
        total2 += maze[idx][4-idx]
    if total2 ==0:
        answer += 1
    if answer >=3:
        return 1

    return -1

maze = []
for _ in range(5):
    line = list(map(int, input().split()))
    maze.append(line)

cnt = 0
flag = True
for _ in range(5):
    sub_list = list(map(int, input().split()))
    if not flag:
        break
    for b in sub_list:
        if not flag:
            break
        cnt +=1
        for i in range(5):
            for j in range(5):
                if maze[i][j]==b:
                    maze[i][j] = 0
        ans = check(maze)
        if ans ==1:
            print(cnt)
            flag = False
            break
