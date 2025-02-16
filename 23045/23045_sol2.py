import sys
sys.stdin = open("23045_input.txt")
T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [None for _ in range(N+1)]

    for num in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val
    for idx in range(N, 0, -1):
        parent_idx = idx//2
        if tree[parent_idx] ==None:
            tree[parent_idx] = tree[idx]
        else:
            tree[parent_idx] += tree[idx]
    print(f"#{test_case} {tree[L]}")