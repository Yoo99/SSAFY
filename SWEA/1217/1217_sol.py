import sys
sys.stdin = open("1217_input.txt")

def recur(N,M):
    global total
    if M ==0:
        return total
    total *= N
    recur(N, M-1)

for test_case in range(1, 11):
    _ = int(input())
    N, M = map(int, input().split())
    total  =1
    recur(N, M)
    print(f"#{test_case} {total}")
