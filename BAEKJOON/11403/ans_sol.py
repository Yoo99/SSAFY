import sys
sys.stdin = open("11403_input.txt")

while True:
    try:
        N = int(input())
    except:
        break
    if N:
        arr = [list(map(int, input().split())) for _ in range(N)]
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if arr[i][k] and arr[k][j]:
                        arr[i][j] =1
        for i in range(N):
            print(*arr[i])