import sys
sys.stdin = open("1248_input.txt")
from collections import defaultdict

def dfs(node, depth):
    visited[node] = True
    depths[node] = depth
    for child in tree[node]:
        if not visited[child]:
            parent[child] = node
            dfs(child, depth+1)
    subtree_size[node] = 1
    for child in tree[node]:
        subtree_size[node] += subtree_size[child]

def lca(a,b):
    while depths[a] != depths[b]:
        if depths[a] > depths[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a!= b:
        a = parent[a]
        b = parent[b]
    return a



T  = int(input())
for test_case in range(1, T+1):
    V,E, node1, node2 = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = defaultdict(list)
    for i in range(0, len(edges), 2):
        tree[edges[i]].append(edges[i+1])
    # print(tree)

    parent = [0] * (V+1)
    depths = [0] * (V+1)
    visited = [False] * (V+1)
    subtree_size = [0] * (V+1)

    dfs(1,0)
    ans = lca(node1, node2)
    print(f"#{test_case} {ans} {subtree_size[ans]}")