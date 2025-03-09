import sys
sys.stdin = open("1959_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M= map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int ,input().split()))
    diff = abs(N-M)
    if len(A)>len(B):
        long_list ,short_list = A,B
    else:
        long_list,short_list = B,A
    total_sum = []
    for i in range(diff+1):
        sum_cnt = 0
        long_list_a = long_list[i:]
        for idx in range(len(short_list)):
            sum_cnt += (short_list[idx] * long_list_a[idx])
        total_sum.append(sum_cnt)
    print(f"#{test_case} {max(total_sum)}")