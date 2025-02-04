import sys

sys.stdin = open("1231_input.txt", "r")


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, num):
        self.tree = [None] + [i for i in range(1, num + 1)]

    def set_value(self, idx, value, left_idx=None, right_idx=None):
        self.tree[idx].value = value
        if left_idx:
            self.tree[idx].left = self.tree[left_idx]
        if right_idx:
            self.tree[idx].right = self.tree[right_idx]


    def inorder(self, node = None):
        if node is None:
            node = self.tree[1]
        if node:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)


bt = BinaryTree(8)
print(bt.tree)
bt.inorder()

# for i in range(1,len(bt.tree)):
#     bt.left = bt.get_left_child(i)
#     bt.right = bt.get_right_child(i)

