
import heapq
numbers = [9,4,12,3,7,8,11]

heapq.heapify(numbers)
print(numbers)
heapq.heappush(numbers, -1)
print(numbers)
smallest = heapq.heappop(numbers)
print(smallest)
