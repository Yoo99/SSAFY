import sys
sys.stdin = open("1954_input.txt")

direction = [(0,1),(1,0),(0,-1), (-1,0)]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cnt = 0
    print(f"#{test_case}")
    arr=[[0] * N for _ in range(N)]
    cnt = 1
    i,j = 0,0
    idx = 0
    arr[0][0] = cnt
    while cnt<N*N:
        dx,dy = direction[idx%4]
        if 0<=(i+dx)<N and 0<=(j+dy)<N and arr[i+dx][j+dy]==0:
            cnt += 1
            i, j = i+dx, j+ dy
            arr[i][j] = cnt
        else:
            idx +=1
    for row in arr:
        print(*row)