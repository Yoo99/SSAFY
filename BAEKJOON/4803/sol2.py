import sys
sys.stdin = open("4803_input.txt")

def find_tree(node, graph):
    global groupy
    visited[node] = True
    groupy.append(node)
    for child in graph[node]:
        if child and not visited[child]:
            find_tree(child, graph)
        elif child and child in groupy:
            groupy = []
            return
test_case = 0
while True:
    N, M = map(int, input().split())
    if N>0 and M>0:
        test_case +=1
        graph = {key: [] for key in range(1, N+1)}
        for _ in range(M):
            a,b = map(int, input().split())
            graph[a].append(b)
        visited = [False for _ in range(N+1)]
        forest = []
        for key in graph.keys():
            if not visited[key]:
                groupy = []
                find_tree(key, graph)
                if groupy:
                    forest.append(groupy)
        ans = 0
        for i in forest:
            if len(i)>0:
                ans +=1
            else:
                continue
        if ans ==0:
            print(f"Case {test_case}: No trees.")
        elif ans == 1:
            print(f"Case {test_case}: There is one tree.")
        else:
            print(f"Case {test_case}: A forest of {ans} trees.")
    else:
        break
