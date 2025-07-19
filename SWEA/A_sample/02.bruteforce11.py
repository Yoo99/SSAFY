import sys
sys.stdin = open("02.input.txt")
import heapq

T = int(input()) # test case의 개수
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # 전체 칸의 수, 기준점 M
    arr = list(map(int, input().split()))
    jewerly = [idx for idx in range(len(arr)) if arr[idx] == 1]
    define = [False for _ in range(N)]
    # 기준점을 기준으로 기준점보다 작은 숫자들의 집합
    for i in range(M-1, -1, -1): # 기준점부터 0번째까지 하나씩 줄여나감
        cnt = 0 # 보석 collect
        dx = i
        jewerly_copy = jewerly[:] # 보석 위치 복제본

        while cnt <= len(jewerly):
            # print("dx", dx, "len_jewerly", len(jewerly))
            # 성공적으로 모든 보석을 취득한 경우 종료하기
            if cnt == len(jewerly): # 기저조건
                break
            # 만약에 내가 현재 있는 위치에서 가장 가까운 보석의 위치 확인
            subset = []
            dist = []
            for idx in jewerly_copy:
                heapq.heappush(subset, (abs(dx-idx),idx))
                dist.append(abs(dx-idx))
            # print(dist)
            if len(set(dist))< len(dist):
                break
            _, idx = heapq.heappop(subset)
            cnt +=1
            jewerly_copy.remove(idx)
            dx = idx
        if cnt == len(jewerly):
            define[i] = True
    # 기준점을 기준으로 기준점보다 큰 숫자들의 집합
    for i in range(M, N, 1): # 기준점부터 0번째까지 하나씩 늘려나감
        cnt = 0 # 보석 collect
        dx = i
        jewerly_copy = jewerly[:] # 보석 위치 복제본
        while cnt <= len(jewerly):
            # print("dx", dx, "len_jewerly", len(jewerly))
            # 성공적으로 모든 보석을 취득한 경우 종료하기
            if cnt == len(jewerly): # 기저조건
                break
            # 만약에 내가 현재 있는 위치에서 가장 가까운 보석의 위치 확인
            subset = []
            dist = []
            for idx in jewerly_copy:
                heapq.heappush(subset, (abs(dx-idx),idx))
                dist.append(abs(dx-idx))
            # print(dist)
            if len(set(dist))< len(dist):
                break
            _, idx = heapq.heappop(subset)
            cnt +=1
            jewerly_copy.remove(idx)
            dx = idx
        if cnt == len(jewerly):
            define[i] = True
    for idx in range(len(define)):
        if define[idx]:
            define[idx] = abs(M-1 - idx)
        else:
            define[idx] = 10000000000
    print(f"#{test_case} {min(define)}")