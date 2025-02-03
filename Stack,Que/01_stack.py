# stack 자료 구조 구현 -> class로 구현
class Stack:
    # stack은 자료를 얼마나 저장할 수 있을지 크기를 지정
    # 기본인자 사용해서, 사용자가 별도의 크기를 지정하지 않을 때에도, 최대 10칸의 stack
    def __init__(self, capacity = 10):
        self.capacity = capacity # 용량
        self.items = [None] * capacity # 스택 요소를 저장할 리스트
        self.top = -1 #  stack의 최초 top은 -1, -1이라는 것은 아직 아무런 연산이 일어나지 않았음을 의미
    def push(self, item):
        self.top +=1
        self.items[self.top] = item
    def peek(self):
        return self.items[self.top]
    def pop(self): # stack에서 top 번쩨 요소를 제거
        item = self.peek()
        self.items[self.top]  = None
        self.top -=1
        return item

stack = Stack(5)
print(stack.items, stack.top)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.items)
print(stack.peek())
print(stack.pop())
print(stack.items)
# Last in First Out : top 번째 요소를 꺼내오는 것이 목표이다.
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)