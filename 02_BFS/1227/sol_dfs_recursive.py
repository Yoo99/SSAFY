import sys
sys.stdin = open("input.txt")


# 파이썬은 재귀함수를 기본적으로 1000번 스택에 쌓이면 멈추게 함.
'''
    최대 재귀 가능 횟수 바꿀 수 있음. 
    sys.setrecursionlimit(100000) 이거를 엄청 크게 만들면 돌아는 간다. 
'''
# RecursionError: 발생함
def search(x,y):
    global result
    for dx, dy in [(-1,0),(1,0),(0,-1), (0,1)]:
        nx = x + dx
        ny = y+dy
        # 모든 모서리 1로 둘러쌓여 있어서, 범위 벗어날 일 없다.
        # 1. 다음 위치가 벽이 아니면
        if data[nx][ny] != 1:
            if data[nx][ny] ==3: # 도착하면
                result = 1 # 전역 변수 변경
                # return 1         # 도착했다는 정보를 반환한다
            data[nx][ny] = 1
            # check = search(nx,ny)
            # if check:
            #     return
    '''
    재귀 함수에서 호출 받은 결과로 return 하는 상황은 
    돌아온 시점에서 바로 종료해야 하는 특별한 상황, 
    혹은 재귀 함수 호출 결과 값으로 연산하여 재 호출해야 하는 상황이다
    -> 피보나치 수열 등 ..
    '''
    # 여기서 0을 반환하는게 맞아?
    # 문제는 도착지에 도착을 하더라도 search를 부르기 때문에 search(x,y)가 실행되고 그러면
    # 당연히 도착점이 없어졌기 때문에 0이 반환된다.
    # return 0



for _ in range(10):
    tc = int(input())
    data = [list(map(int, input())) for _ in range(100)]
    # 1: 벽, 0: 길, 2: 출발점, 3: 도착점.
    result = 0 # 도착지에 도착할 수 있는지 정보
    # BFS로 그래프를 탐색할 건데, 시작 정점이 어디인지 모르는 상황
    # -> BFS를 정의할 때, 시작 정점의 좌푯값을 넘겨 받을 수 있도록 만들어주자.
    # 시작 정점이 어딘지 찾아 나가야 한다.
    for x in range(100):
        for y in range(100):
            if data[x][y] ==2: # 출발지라면
                # 약속, 조사 도중, 도착지에 도달하면 True 반환해주기
                result = search(x,y) # 해당 위치에서 출발
                # 밑의 break는 본인이 속해있는 for문에 대해서만 정지
                break  # 출발지가 하나밖에 없으니 한번 조사했으면 끝.
        if result: # 만약, 목적지에 도착했다면, result를 1로 바꿀 것
            break # 그렇게 어떤 경우든 result가 1이 되면 break
    print(result)
    '''
    조사의 상황을 상하좌우 중 어디를 먼저 할 것인지를 if 문으로 달 수 있고 
    이것이 바로 백트래킹의 개념이다. 
    BFS 는 최단 경로를 얻을 수 있다. 해당 목적지를 갈 수 있는 길인지를 확인하기 
    위해서 모든 가능한 경로를 가기 때문에 오래 걸릴 수는 있으나 도착하는 시점에
    종료가 된다. 
    '''
