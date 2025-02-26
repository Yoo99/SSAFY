import sys
sys.stdin = open("5684_input.txt")


def find(node):
    global road
    road.append(node)
    for child in graph[node]:
        if child in road:
            road.append(child)
            return
        else:
            find(child)

T = int(input())
for test_case in range(1, T+1):
    N, M=  map(int, input().split())
    arr = []
    keys = [n for n in range(1, N+1)]
    graph = {key:[] for key in keys}
    length = {}
    for i in range(M):
        line = list(map(int, input().split()))
        node1, node2 = line[0], line[1]
        length[(node1, node2)] = line[-1]
        graph[line[0]].append(line[1])
    final_path = []
    for key in graph.keys():
        road = []
        find(key)
        final_path.append(road)
    min_length = 30
    for ele in final_path:
        if len(ele) <min_length:
            min_length = len(ele)
    for ele in final_path:
        if len(ele) == min_length:
            continue
        else:
            final_path.remove(ele)
    sum_path  = 100000000
    for ele in final_path:
        sum_val = 0
        for i in range(0, len(ele)-1):
            node1, node2 = ele[i], ele[i+1]
            if length[(node1, node2)]:
                sum_val += length[(node1,node2)]
            else:
                break
        if sum_val<sum_path:
            sum_path =sum_val
    print(f"#{test_case} {sum_path}")


