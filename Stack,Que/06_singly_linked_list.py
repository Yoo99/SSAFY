class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # 내 다음 요소가 위치할 공간
class SinglyLinkedList:
    def __init__(self):
        self.head = None #  첫 번째 요소를 가리킬 head
    # data : 삽입할 데이터
    # position : 삽입할 위치
    def insert(self, data, position):
        # 새로운 노드를 생성
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            # 현재 위치는 SLL 시작지점
            current = self.head
            # 내가 삽입하고자 하는 위치에 도달할 때까지 순회
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next=  new_node
