import sys
sys.stdin = open("2930_input.txt")

import heapq

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    queue = []
    result = []
    for i in range(N):
        arr = list(map(int, input().split()))
        if len(arr)==2:
            heapq.heappush(queue, -arr[1])
        else:
            if queue:
                result.append(-heapq.heappop(queue))
                ans = 0
            else:
                result.append(-1)
    final = ''
    for b in result:
        final += str(b) + " "
    print(f"#{test_case} {final}")