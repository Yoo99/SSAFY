import sys
sys.stdin = open("14413_input.txt")

direction = [(-1,0), (0,-1), (1,0),(0,1)]

T = int(input())
for test_case in range(1, T+1):
    N, M=  map(int,input().split())
    arr = []
    for _ in range(N):
        line=  list(input())
        arr.append(line)

    case1 = [[0]*M for _ in range(N)]
    case2 = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if (i+j)%2 == 0:
                case1[i][j] = '#'
                case2[i][j] = '.'
            else:
                case1[i][j]='.'
                case2[i][j] = '#'
    flag_one ,flag_two = True, True
    for i in range(N):
        for j in range(M):
            if arr[i][j]!='?':
                if arr[i][j] ==case1[i][j]:
                    continue
                else:
                    flag_one = False
        if not flag_one:
            break
    if flag_one:
        print(f"#{test_case} possible")
        continue
    for i in range(N):
        for j in range(M):
            if arr[i][j]!='?':
                if arr[i][j] == case2[i][j]:
                    continue
                else:
                    flag_two = False
        if not flag_two:
            break
    if not flag_two:
        print(f"#{test_case} impossible")
        continue
    else:
        print(f"#{test_case} possible")