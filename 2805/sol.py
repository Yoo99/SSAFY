import sys

sys.stdin = open('input.txt', 'r')


tc = int(input())
for test_case in range(1, tc+1):
    N = int(input())
    arr = []
    for i in range(N):
        line = input()
        # print(line)
        arr.append(list(line))
    mid = (N+1)//2 -1
    sum = 0
    for b in arr[mid][:]:
        sum += int(b)
    for i in range(0, mid):
        for j in range(mid-i,mid+i+1):

            sum += int(arr[i][j])
            sum += int(arr[N-i-1][j])
    print(f"#{test_case} {sum}")