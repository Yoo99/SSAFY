import sys
sys.stdin = open("19113_input.txt")
from collections import deque

T = int(input())
for test_case in range(1, T+1):
    n = int(input()) # 상품의 개수
    price = list(map(int, input().split()))
    price.reverse()
    queue = deque(price)
    old_price = []
    new_price = []
    while queue:
        b = queue.popleft()
        if len(new_price)==n:
            break
        if b*3//4 in price:
            old_price.append(b)
            new_price.append(b*3//4)
            queue.remove(b*3//4)

    new_price.sort()
    print(f"#{test_case} ", end = "")
    print(*new_price)