import sys
sys.stdin = open("9280_input.txt")
from collections import deque

T = int(input())
for test_case in range(1, T+1):
    n,m = map(int, input().split())
    price = [0 for _ in range(n)] # 주차 자리별 요금 리스트
    weight = [0 for _ in range(m+1)]
    for i in range(n):
        price[i] = int(input())
    for j in range(1,m+1):
        weight[j] = int(input())
    space = [0 for _ in range(n)]
    # 차가 들어오고 나가는 로직
    total_price = 0
    waiting_line = deque([])

    for _ in range(2*m):
        space_list = [i for i in range(n) if space[i]==0]
        car_num = int(input())
        if car_num>0:
            waiting_line.append(car_num)
            if len(space_list)>0:
                idx = min(space_list)
                space[idx] = waiting_line.popleft()
        elif car_num <0:
            car_idx = car_num * (-1)
            index = space.index(car_idx)
            total_price += price[index] * weight[car_idx]
            space[index] = 0
            space_list = [i for i in range(n) if space[i]==0]
            if waiting_line and len(space_list)>0:
                idx = min(space_list)
                space[idx] = waiting_line.popleft()
    print(f"#{test_case} {total_price}")
