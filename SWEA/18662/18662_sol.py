import sys
sys.stdin = open("18662_input.txt")

T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int ,input().split()))
    ele = (arr[0] + arr[-1])/2
    ans = arr[1] - ele
    print(f"#{test_case} {abs(ans)}")