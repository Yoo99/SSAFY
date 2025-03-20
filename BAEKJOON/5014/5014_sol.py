import sys
sys.stdin = open("5014_input.txt")

F,S,G,U,D = map(int, input().split())
# F : 전체 층 높이, S : 강호가 현재 있는 층,
# G : 이동하려는 층 , U : 위로 올라가는 단위, D : 아래로 내려가는 단위

visited = [False for _ in range(F+1)]
visited[0] = True
Flag = True
cnt = 0
ans = "use the stairs"
direction = [U,-D]
while S!=G:
    # if visited[S]:
    #     Flag = False
    #     break
    print(S)
    if S == G:
        ans = cnt
        break
    elif S<G and (S+U)<=F and :
        S = S+U
        if not visited[S]:
            visited[S] = True
            cnt +=1
        else:
            S -=D
    elif S>G and (S-D)>=0:
        S -= D
        if not visited[True]:
            visited[S] = True
            cnt +=1
        else:
            S +=U
print(ans)




