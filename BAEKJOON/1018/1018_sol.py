import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
maze = []
for row in range(N):
    line=  list(map(str, input()))
    maze.append(line)

case1 = [["A" for _ in range(M)] for _ in range(N)]
case2 = [["A" for _ in range(M)] for _ in range(N)]
for idx in range(N):
    for idy in range(M):
        if (idx + idy) %2 ==1:
            case1[idx][idy] = "B"
            case2[idx][idy] = "W"
        else:
            case1[idx][idy] = "W"
            case2[idx][idy] = "B"
min_count = float('inf')
for row in range(0, N-7):
    for col in range(0,M-7):
        count1, count2 = 0,0
        for idx in range(row, row + 8):
            for idy in range(col, col + 8):
                if maze[idx][idy] != case1[idx][idy]:
                    count1 +=1
                if maze[idx][idy] != case2[idx][idy]:
                    count2 += 1
        if min_count > min(count1, count2):
            min_count  =min(count1, count2)

print(min_count)