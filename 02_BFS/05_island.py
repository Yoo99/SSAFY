import sys
from collections import deque
sys.stdin = open("input2.txt", "r")

# 관성으로 풀이하지 말기
# from은 언제 할거냐? 진짜 그 모듈 라이브러리 프레임워크가 필요할 때 불러올 것
# views.py 파일 열자마자 일단 from 적어 XXXXXXXX
# 이렇게 하면 디버깅 절대 못함.
N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]
result = 0
# 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
dx = [-1, 1, 0, 0,-1, -1,1,1]
dy = [0, 0, -1, 1,-1,  1,-1,1]

def find_island(x,y):
    global cnt
    queue = deque([(x,y)])
    data[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for k in range(8):
            nx,ny = x + dx[k], y + dy[k]
            # 갈 수 있는 경우들에 대해서 조건 => 길어
            # 갈 수 없으면 후보가 못 되네? 넘어가
            # 범위 벗어나면 아무것도 하지마
            if 0>nx or nx>=N or 0>ny or ny>=M:
                continue
            # 다음좌표 위치가 0이라면
            if data[nx][ny] ==0:
                continue
            # 위 모든 if를 무시하고 왔다? -> 조사 가능 대상이다.
            queue.append((nx,ny))
            data[nx][ny] = 0
    cnt +=1


# 시작 지점이 어디지?
# 내가 가진 모든 data에 대해서 1로 시작하는 값 모든 곳에서 조사
# 완전 탐색
# 하나 이상의 1로 구성된 값들을 세어야 한다.
cnt = 0
for x in range(N):
    for y in range(M):
        # 일단 땅인 곳에서 조사를 시작해
        if data[x][y] ==1:
            # 아까는 시작 좌표가 고정이어서 인자 없어도 됐음
            # 이번엔 시작 좌표가 매번 달라짐
            find_island(x,y)
print(cnt)