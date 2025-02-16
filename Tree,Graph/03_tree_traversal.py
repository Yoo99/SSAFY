class TreeNode:
    def __init__(self, value):
        self.value =value
        self.left=  None
        self.right=  None

def preorder(node):
    if node:
        # 전위 순회는 대상 노드 도달하자마자 할 일 실행
        print(node.value, end = ' ')
        # 왼쪽 자식을 조사하러 가는 것
        preorder(node.left)
        preorder(node.right)

root = TreeNode('A')
root.left =TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
# preorder(root)

# 중위 순회
def inorder(node):
    if node:
    #중위 순회는 왼쪽 자시긍ㄹ 먼저 조사하고, 돌아와서 할일을 실행한다.
        inorder(node.left)

        print(node.value, end = ' ')
        inorder(node.right)
# inorder(root)

# 후위 순회
def postorder(node):
    if node:
        # 후위 순회는 왼쪽, 오른쪽 자식을 먼저 조사하고 돌아와서 할일을 실행한다.
        postorder(node.left)
        postorder(node.right)
        print(node.value, end = ' ')
postorder(root)