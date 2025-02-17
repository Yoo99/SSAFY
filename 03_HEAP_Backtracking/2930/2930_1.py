import sys
import heapq
sys.stdin = open("2930_input.txt")


T = int(input()) # 테스트 케이스
for test_case in range(1, T+1):
    N = int(input())
    heap = []
    result = []
    for i in range(N):
        line = list(map(int, input().split()))
        if len(line)>1:
            heapq.heappush(heap,-line[1])
        else:
            if len(heap)==0:
                result.append(-1)
            else:
                result.append(-heapq.heappop(heap))
    ans = *result
    print(f"#{test_case} {result}")