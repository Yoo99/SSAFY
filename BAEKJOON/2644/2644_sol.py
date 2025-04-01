import sys
sys.stdin = open("2644_input.txt")

def find_rel(node):
    global cnt
    global b
    global Flag
    visited[node] = True
    cnt += 1
    if node == int(b):
        Flag = True
        return cnt
    for child in graph[node]:
        if not visited[child]:
            if child != b:
                find_rel(child)
            elif child == b:
                Flag = True
                return cnt
<<<<<<< HEAD
            break
=======
>>>>>>> 850ebaf97aaf360d184ea05110e018523e8b19e6
    return cnt, Flag

N = int(input()) # 전체 사람의 수
graph = {key:[] for key in range(1, N+1)}
a,b = map(int,input().split()) # 관계를 비교해야 할 두 사람이 주어짐
m = int(input()) # 관계의 개수
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
cnt = 0
visited = [False for _ in range(N+1)]
Flag = False
cnt, Flag = find_rel(a)
<<<<<<< HEAD
=======
print(cnt, Flag)
>>>>>>> 850ebaf97aaf360d184ea05110e018523e8b19e6
if Flag ==True:
    print(cnt)
else:
    print(-1)