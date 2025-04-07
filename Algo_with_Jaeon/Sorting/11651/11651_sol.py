import sys
sys.stdin = open("11651_input.txt")
import heapq

T = int(input())
hq = []
for _ in range(T):
    x,y = map(int, input().split())
    heapq.heappush(hq,(y,x))
while True:
    try:
        d,e = heapq.heappop(hq)
        print(e,d)
    except:
        break