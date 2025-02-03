from collections import deque

# double ended queue
# 이중 연결리스트 처럼 되어 있는 친구
queue = deque()
queue.append((1,1))
queue.append((2,2))
queue.append((3,3))
print(queue)
print(queue.popleft())
print(queue)