# 노드 하나의 객체 정보를
class TreeNode:
    def __init__(self, value):
        self.value = value  # 노드의 값을 저장
        self.left = None
        self.right = None



class BinaryTree:
    def __init__(self):
        # 최소 한개 이상의 노드로 구성
        self.root = None
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value) # 트리가 비었으면 직접 삽입
        else:
            # 루트 노드부터 삽입 가능한 노드를 찾아서 삽입한다.
            self._insert_recursive(self.root, value)

    # 특정한 조건을 만족했을 때에는 객체 생성 후 삽입
    # 그렇지 않은 경우,
    def _insert_recursive(self, node, value):
        if value <node.value: # 내가 삽입하고자 하는 값이 node의 value보다 작을 때에만 왼쪽에다가 넣는 것
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

bt = BinaryTree()
bt.insert(5) # 5를 삽입
print(bt.root)
print(bt.root.value)
bt.insert(3)
bt.insert(6)
print(bt.root.left.value) # 왼쪽 자식으로 변경이 되었음을 알 수 있음
print(bt.root.right.value)

bt.insert(4)
print(bt.root.left.right.value)
# print(bt.root.right.value)