import sys
from collections import deque
sys.stdin = open("1267_input.txt", "r")

def dfs(node):
    for child in graph.get(node):
        queue.append(child)
        dfs(child)

for test_case in range(1,11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(arr)
    dict_key = list(set(arr))
    visited = [False] * (max(dict_key)+1)
    # print(visited)
    graph = {key:[] for key in dict_key}
    # print(graph)
    for r in range(0, len(arr), 2):
        v, e = arr[r], arr[r+1]
        graph[v].append(e)
    print(graph)
    queue = deque([])
    # for key, val in graph.items():
    #     queue.append(key)
    #     if val!=[]:
    #         queue.extend(val)
    #     else:
    #         continue
    # key_list = graph.keys()
    #
    # for key in key_list:
    #     dfs(key)
    #
    # ans = []
    # for ele in queue:
    #     if visited[ele] == False:
    #         visited[ele] = True
    #         ans.append(ele)
    #     else:
    #         continue
    # print(f"#{test_case}", end = '')
    # for d in ans:
    #     print("", d, end = '')
    # print()
