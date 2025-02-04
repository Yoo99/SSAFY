# 노드 하나의 객체 정보를
class TreeNode:
    def __init__(self,value):
        self.value = value # 노드의 값을 저장
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
            # 루트 노드부터 삽입 가능한 노드를 찾아서 삽입
            self._insert_recursive(self.root, value)
    def _insert_recursive(self, node, value):
        if value < node.value:
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
bt.insert(5)
print(bt.root.value)
bt.insert(3)
bt.insert(6)
print(bt.root.left.value)
print(bt.root.right.value)
bt.insert(4)
print(bt.root.left.right, bt.root.left.right.value)