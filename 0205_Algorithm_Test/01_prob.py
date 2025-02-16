import sys
sys.stdin = open("prob1_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N: 가로, M : 세로
    arr = []
    for i in range(N):
        line = list(map(int, input().split()))
        arr.append(line)
    parking_lot = []
    for row in range(N-1):
        for col in range(M-1):
            sub = []
            sub.append(arr[row][col])
            sub.append(arr[row][col+1])
            sub.append(arr[row+1][col])
            sub.append(arr[row+1][col+1])
            if 0 in sub:
                continue
            else:
                parking_lot.append(sum(sub))
    print(f"#{test_case} {min(parking_lot)}")