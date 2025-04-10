import sys
sys.stdin = open("1959_input.txt")

T = int(input()) # test case의 개수
for test_case in range(1, T+1):
    max_sum = 0
    N,M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2=  list(map(int, input().split()))
    if N>M:
        long, short = arr1, arr2
    else:
        long , short = arr2, arr1
    for j in range(len(long)- len(short)+1):
        temp = 0  # 임시 합계 값을 넣어둘 변수
        for i in range(len(short)):
            # print(j, i)
            temp += (short[i] * long[j+i])
        if temp >max_sum:
            max_sum = temp
    print(f"#{test_case} {max_sum}")