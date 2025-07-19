import sys
sys.stdin = open("5432_input.txt")
from collections import deque

T = int(input()) # test case의 개수
for test_case in range(1, T+1):
    arr = deque(map(str, input()))
    suffix = []
    total = 0
    cnt = 0
    sub_total =  0
    # print(len(arr))
    for i in range(len(arr)):
        if arr[i] == "(":
            cnt +=1
        elif arr[i] ==")":
            if arr[i-1] == "(":
                cnt -=1
                total += cnt
            elif arr[i-1]==")":
                cnt -= 1
                sub_total +=1
    print(f"#{test_case} {sub_total+total}")