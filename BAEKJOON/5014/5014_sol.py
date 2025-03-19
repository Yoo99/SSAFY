import sys
sys.stdin = open("5014_input.txt")

F,S,G,U,D = map(int, input().split())
# F : 전체 층 높이, S : 강호가 현재 있는 층,
# G : 이동하려는 층 , U : 위로 올라가는 단위, D : 아래로 내려가는 단위

visited = [False for _ in range(F+1)]
visited[0] = True
Flag = True
while Flag:
    if