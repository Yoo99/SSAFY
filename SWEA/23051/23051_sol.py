import sys
sys.stdin = open("23051_input.txt")

def find_group(node, graph):
    global groupy
    global final_group
    visited[node] = True
    groupy.append(node)
    for child in graph[node]:
        if child!= []  and not visited[child]:
            find_group(child, graph)
        elif child!=[] and visited[child]:
            for ele in final_group:
                if child in ele:
                    ele.append(node)
                    groupy.remove(node)
                else:
                    continue
        else:
            return


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    graph = {key: [] for key in range(1, N+1)}
    arr = list(map(int, input().split()))
    for i in range(0, len(arr), 2):
        graph[arr[i]].append(arr[i+1])
    visited = [False for _ in range(N+1)]
    final_group = []
    for key in graph.keys():
        if not visited[key]:
            groupy = []
            find_group(key, graph)
            if not groupy:
                continue
            else:
                final_group.append(groupy)
        else:
            continue

    print(f"#{test_case} {len(final_group)}")