class TreeNode:
    def __init__(self, value):
        self.value=  value
        self.left = None
        self.right = None

def preorder(node): # 전위순회
    if node:
        # 전위 순회는 대상 노드 도달하자마자 할 일 실행
        print(node.value, end = ' ')
        # 왼쪽 자식을 조사하러 가는 것
        preorder(node.left)
        preorder(node.right)
    # None이 되면 이전으로 게속 돌아감 : D -> B : E가 출력 -> A : C 가 출력됨
    # C의 왼쪽 오른쪽 탐색하는데 아무것도 없으니 A로 돌아가서 그대로 종료됨

def inorder(node): # 중위 순회
    if node:
        # 왼쪽 자식을 조사하러 가는 것
        # 본인으로 돌아왔을 때 바로 출력하는 것이 아닌 왼쪽으로 갔다가 돌아왔을 때 할일을 하는 것
        inorder(node.left)
        # 돌아와서 할일 실행
        print(node.value, end = ' ')
        inorder(node.right)
def postorder(node):
    if node:
        # 후위 순회는 왼쪽, 오른쪽 자식을 먼저 조사하고
        postorder(node.left)
        postorder(node.right)
        # 돌아와서 할일을 수행
        print(node.value, end = ' ')

root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
preorder(root)
print()
inorder(root)
print()
postorder(root)