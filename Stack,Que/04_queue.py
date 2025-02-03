class Queue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.rear == self.front
    # 값 삽입
    def enqueue(self,item):
        self.rear +=1
        self.items[self.rear] = item
    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        self.front += 1
        item = self.items[self.front]
        return item

queue = Queue(5)
queue.enqueue('A')
print(queue.items)
print("===== dequeue ======")
print(queue.dequeue())
print(queue.front, queue.rear)
print(queue.is_empty())
