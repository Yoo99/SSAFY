import heapq

numbers = [9,4,12,3,7,8,11]

max_heap = []
for num in numbers:
    heapq.heappush(max_heap, -num)  # 음수로 변환한 값을 추가
print(max_heap)
largest = -heapq.heappop(max_heap) # 반환 시 다시 음수로 변환
print(largest)