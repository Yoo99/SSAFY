import sys
sys.stdin = open("2606_input.txt")

def find_rel(node):
    global cnt
    visited[node] = True
    for child in comp[node]:
        if not visited[child]:
            cnt +=1
            find_rel(child)
    return cnt

T = int(input()) # 컴퓨터의 수
comp = {key:[] for key in range(T+1)}
N = int(input()) # 컴퓨터 쌍의 관계 개수
for _ in range(N):
    key, val = map(int, input().split())
    # 유방향 그래프가 아님
    comp[key].append(val)
    comp[val].append(key)
visited = [False for _ in range(T+1)]
cnt = 0
print(find_rel(1))