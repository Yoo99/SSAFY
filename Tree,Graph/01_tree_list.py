class BinaryTree:
    def __init__(self):
        self.tree = [
            None, # 0번 노드를 안 쓰기 위해서
            'A','B','C','D','E','F','G','H','I',
            'J','K','L','M'
        ]

    def insert(self, value):
        self.tree.append(value)
    def get_node(self,index):
        if index < len(self.tree):
            return self.tree[index]
    # 특정 위치에 값을 바꾸거나 재할당 하고 싶다.
    def set_node(self, index, value):
        # if index>=len(self.tree):
            # self.insert(value)
        while index>=len(self.tree): # 최대한 이진트리 구조를 깨지 않기 위해서 원하는 인덱스 위치까지 None 값을 넣음
            # 하지만 어찌되었든 이진트리 구조는 깨진 것
            self.tree.append(None)
        self.tree[index] = value
    # 왼쪽 자식을 보고 싶은 경우
    def get_left_child(self, index):
        left_index = index * 2
        if left_index<len(self.tree):
            return self.tree[left_index]

    def get_right_child(self, index):
        right_index = index * 2 +1
        if right_index<len(self.tree):
            return self.tree[right_index]

    def get_parent_node(self, index):
        parent_index = index//2
        if parent_index>=0:
            return self.tree[parent_index]

bt = BinaryTree()
print(bt.tree)
bt.set_node(16, 'Z')
print(bt.tree)
print(bt.get_left_child(2))
print(bt.get_left_child(16))
print(bt.get_right_child(3))
print()