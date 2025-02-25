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
N, M=  map(int, input().split())
arr = []
keys = [n for n in range(1, N+1)]
graph = {key:[] for key in keys}
for i in range(M):
    line = list(map(int, input().split()))
    arr.append(arr)
    graph[line[0]].append(line[1])
print(graph)
final_path = []
for key in graph.keys():
    road = []
    find(key)
    final_path.append(road)
print(final_path)
min_length = 30
for ele in final_path:
    if len(ele) <min_length:
        min_length = len(ele)
print(min_length)