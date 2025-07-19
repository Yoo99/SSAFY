import sys
sys.stdin = open("22654_input.txt")

direction = [(-1,0), (0,1), (1,0),(0,-1)] # 상 우 하 좌

T = int(input()) # test_case의 개수
for test_case in range(1, T+1):
    N = int(input()) # 한 변의 길이
    arr = []
    for _ in range(N):
        line= list(map(str, input()))
        arr.append(line)
    c = int(input()) # 커맨드 횟수
    ans = []
    # 현재 RC 카의 위치
    for i in range(N):
        for j in range(N):
            if arr[i][j] =='X':
                x,y = i,j
                break
    cmd = [] # 커맨드 명령어 넣기
    for _ in range(c): # 커맨드의 횟수
        _, order  = input().split()
        cmd.append(list(order))

    for dt in range(len(cmd)):
        i = 0
        nx, ny = x, y
        for idx in range(len(cmd[dt])):
            if cmd[dt][idx] == 'R':
                i +=1
            elif cmd[dt][idx] =='L':
                i-=1
            elif cmd[dt][idx] == 'A':
                temp_x, temp_y = nx+direction[i%4][0] , ny+direction[i%4][1]
                if 0<=temp_x<N and 0<=temp_y<N and arr[temp_x][temp_y]!='T':
                    nx,ny = temp_x, temp_y
                else:
                    continue
        if arr[nx][ny] == 'Y':
            ans.append(1)
        else:
            ans.append(0)
    print(f"#{test_case} ", end = '')
    print(*ans)
    print()





