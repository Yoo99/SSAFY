import sys
sys.stdin = open("5607_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N,R = map(int, input().split())
    Q_list, S_list = [], []
    if R>N//2:
        R = N-R
    Q_list = [i for i in range(N, N-R, -1)]
    S_list = [i for i in range(1, R+1)]
    Q_rest = [i for i in Q_list if i not in S_list]
    S_rest = [item for item in S_list if item not in Q_list]
    Q,S = 1,1
    for idx in Q_rest:
        Q *= idx
    for idj in S_rest:
        S *= idj
    print(f"#{test_case} {(Q//S)% 1234567891}")
