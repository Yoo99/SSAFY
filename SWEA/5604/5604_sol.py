import sys
sys.stdin = open("5604_input.txt")

T = int(input())
for test_case in range(1, T+1):

    A,B = map(int, input().split())
    arr = [0] * 10  # 0부터 9까지의 수 입력
    for i in range(A, B+1):
        n = list(str(i))
        for b in n:
            arr[int(b)] += 1
    cnt = 0
    for b in range(0, len(arr)):
        cnt += b*arr[b]
    print(f"#{test_case} {cnt}")