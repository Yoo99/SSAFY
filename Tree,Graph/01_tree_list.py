class BinaryTree:
    def __init__(self):
        self.tree = [
            None, 'A','B','C','D','E',
            'F','G','H','I','J','K','L','M'
        ]
    def insert(self, value):
        self.tree.append(value)
    def get_node(self,index):
        if index<len(self.tree):
            return self.tree[index]
    # 특정 위치에 값을 바꾸거나 재할당 하고 싶다.
    def set_node(self, index,value):
        # if index>=len(self.tree):
            # self.insert(value)
        while index >= len(self.tree):
            self.tree.append(None)
        self.tree[index] = value
    # 왼쪽 자식을 보고 싶다
    def get_left_child(self,index):
        left_index = index *2
        if left_index <len(self.tree):
            return self.tree[left_index]

bt= BinaryTree()
print(bt.tree)
bt.set_node(16, 'Z')
print(bt.tree)
print(bt.get_left_child(2))
print(bt.get_left_child(16))
