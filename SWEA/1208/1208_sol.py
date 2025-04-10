import sys
sys.stdin = open("1208_input.txt")
from collections import deque

for test_case in range(1,11):
    N = int(input()) # 덤프 횟수 제한
    cnt = 0
    arr = deque(map(int, input().split()))
    diff = 100
    while cnt<N:
        if cnt == N:
            diff = max(arr) - min(arr)
            break
        elif diff ==0 or diff==1:
            break
        cnt +=1
        max_num = max(arr)
        min_num = min(arr)
        diff = max_num - min_num
        arr.remove(max_num)
        arr.remove(min_num)
        arr.append(max_num-1)
        arr.append(min_num+1)

    print(f"#{test_case} {diff}")


