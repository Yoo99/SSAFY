'''
첫 줄에 테스트 케이스 개수 T, 다음 줄 부터 케이스별로 첫 줄에 N,
다음 N개의 줄에 걸쳐 빈칸으로 구분된 N개의 정수가 주어진다
0이 아닌 숫자는 사과가 나타나는 순서와 위치를 표시한다
우 하 좌 상 순서로 방향을 정해야 한다
'''
import sys
sys.stdin = open("01.apple_input.txt")
import heapq


direction =[(0, 1, 'R'),(1, 0, 'D'), (0,-1, 'L'),(-1,0,'U')] #방향에 대한 정보


def find_apple(d,dx,dy, ax,ay): #현재 내가 바라보고 있는 방향, 현재 내가 있는 위치, 사과 위치
    # 방향 회전을 몇번 해야 하는지 확인하기
    global cnt # 방향 회전 횟수를 기록할 예정
    turn = []
    if dx < ax:
        turn.append('D')
    if dx > ax:
        turn.append('U')
    if dy<ay:
        turn.append('R')
    if dy>ay:
        turn.append('L')
    Flag = True
    while Flag: # 회전해야 할 방향이 남아 있는 경우 지속
        # print("direciton", d,direction[d%4][2],"cnt: ",cnt, turn)
        if not turn:
            Flag = False
            break # 만약에 turn 리스트가 비면 while 문을 종료하기
        if direction[d%4][2] in turn:
            turn.remove(direction[d%4][2])# 회전 리스트에서 제외하기
        elif direction[d%4][2] not in turn:
            d +=1
            cnt +=1
    dx,dy = ax,ay
    return d,cnt, dx,dy

T = int(input()) # test_case의 개수
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    apple = [] # 사과의 위치 정보를 담을 힙큐
    for idx in range(N):
        for idy in range(N):
            if arr[idx][idy] >0:
                heapq.heappush(apple,(arr[idx][idy], idx, idy)) # 사과의 정보를 순서대로 push
    # 방향을 나타내는 변수는 d로 한다 ( d%4 번째 direction 정보를 가지고 한다)
    d, cnt = 0,0 # 방향 인덱스
    dx, dy = 0,0 # 현재 내가 있는 위치
    for apx in range(len(apple)): # 사과의 개수만큼 사과 먹기 함수 실행
        _,ax,ay = heapq.heappop(apple)# N번째 사과가 있는 x ,y 좌표
        d,cnt,dx,dy = find_apple(d, dx,dy, ax,ay)

    print(f"#{test_case} {cnt}")