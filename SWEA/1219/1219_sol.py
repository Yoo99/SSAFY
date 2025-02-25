import sys
sys.stdin = open("1219_input.txt")


from collections import deque

def dfs(node):
    global final
    queue = deque((tree.get(node)))
    while queue:
        children = queue.popleft()
        if children == 99:
            final = 1
            break
        if tree[children] != []:
            for child in tree[children]:
                if child not in queue:
                    queue.append(child)
    return final


for test_case in range(1, 11):
    n, L = map(int, input().split())
    arr = list(map(int, input().split()))
    keys = list(set(arr))
    tree =  {key:[] for key in keys}
    for i in range(0, len(arr), 2):
        tree[arr[i]].append(arr[i+1])

    final = 0
    print(f"#{test_case} {dfs(0)}")
