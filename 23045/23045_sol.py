import sys
sys.stdin = open("23045_input.txt", "r")

class BinaryTree:
    def __init__(self,num):
        self.tree = [None for _ in  range(num)]
    def insert(self, index, value):
        if index<=len(self.tree):
            self.tree[index] = value


T = int(input())
for test_case in range(1, T+1):
    N,M,L = map(int, input().split())
    bt = BinaryTree(N + 1)
    for i in range(M):
        idx, val = map(int, input().split())
        bt.insert(idx, val)
    for b in range(len(bt.tree)-1, -1,-1):
        if bt.tree[b]!=None:
            subidx = b//2
            if bt.tree[subidx] ==None:
                bt.tree[subidx] = bt.tree[b]
            else:
                bt.tree[subidx] += bt.tree[b]
    print(f"#{test_case} {bt.tree[L]}")

