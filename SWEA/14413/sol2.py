import sys
sys.stdin = open("14413_input.txt")

direction = [(-1,0), (0,-1),(1,0),(0,1)]

# ? 가 아닐때 탐색할 함수
def func1(x,y):
    global final_flag
    for dx, dy in direction:
        nx, ny = dx+x, dy+y
        if 0<=nx<N and 0<=ny<M:
            if arr[nx][ny]!=arr[x][y]:
                continue
            else:
                final_flag = False
                return final_flag
    return final_flag

T = int(input())
for test_case in range(1, T+1):
    N ,M = map(int, input().split())
    arr = []
    for _ in range(N):
        line=  list(input())
        arr.append(line)
    updated = True
    while updated:
        updated = False
        for i in range(N):
            for j in range(M):
                if arr[i][j] == '?':
                    subset = []
                    for dx, dy in direction:
                        nx,ny= i+dx, j+dy
                        if 0<=nx<N and 0<=ny<M and arr[nx][ny] !='?':
                            subset.append(arr[nx][ny])
                    if len(set(subset))==1:
                        updated = True
                        if subset[0] =='#':
                            arr[i][j] = '.'
                        else:
                            arr[i][j] = '#'
    if any('?' in row for row in arr):
        print(f"#{test_case} impossible")
        continue

    final_flag = True
    for i in range(N):
        for j in range(M):
            func1(i,j)
            if final_flag == False:
                break
            else:
                continue
        if final_flag == False:
            break

    if final_flag:
        print(f"#{test_case} possible")
    else:
        print(f"#{test_case} impossible")