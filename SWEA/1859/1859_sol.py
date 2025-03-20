import sys
sys.stdin = open("1859_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 날짜 개수
    price = list(map(int, input().split()))
    max_price, profit = 0, 0
    for idx in range(N-1, -1, -1):
        if price[idx]>max_price:
            max_price = price[idx]
        else:
            profit += (max_price - price[idx])

    print(f"#{test_case} {profit}")