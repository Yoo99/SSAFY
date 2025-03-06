import sys
sys.stdin = open("14510_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    M = max(data)
    diffs = [M - i for i in data]

    if sum(diffs) ==0:
        print(f"#{test_case} 0")
        continue
    # 각 나무가 홀수 날의 +1을 꼭 받아야 하는 경우의 수
    odd = sum(1 for d in diffs if d % 2 == 1)
    x = odd

    while True:
        ones = (x+1)//2  # x일 중 홀수 날의 수
        twos = x //2     # x일 중 짝수 날의 수

        if ones < odd:
            x += 1
            continue

        even = sum(d//2 for d in diffs)
        if twos + (ones - odd) // 2 >= even:
            print(f"#{test_case} {x}")
            break
        x += 1
