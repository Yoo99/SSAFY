import sys
sys.stdin = open("2817_input.txt")

def backtracking( idx, subset_sum):
    global count
    global arr

    if subset_sum==K:
        count+=1
        return
    if subset_sum>K:
        return

    for i in range(idx, N):
        print("i",i, "idx",idx)
        plus = arr[i]
        backtracking(i+1, subset_sum+plus)


T = int(input())
for test_case in range(1, T+1):
    N,K= map(int, input().split())
    count = 0
    arr = list(map(int, input().split()))
    backtracking( 0, 0)
    print(f"#{test_case} {count}")