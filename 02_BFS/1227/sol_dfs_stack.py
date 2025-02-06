#dfs stack 방식으로 해결하기
import sys
# 미로나 길찾기 등은 DFS를 사용하는 것이 좋다
# 최단 경로 1번만 검색하면 된다라고 한다면 BFS를 사용하는 것이 나을 수도 있음.
sys.stdin = open('input.txt')


def search(x, y):
    # queue를 stack으로 바꿈. 외 변동사항 없음
    stack =[(x,y)]
    visited = [[0] * 100 for _ in range(100)]
    while stack:
        x, y = stack.pop(0)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            # 습관적으로 코드 적기
            # 1. 범위를 벗어나지 않고
            # 2. 0(길)인 경우만 이동
            # 아래 조건은 이번 문제에서는 필요가 없다.
            # 아래 조건을 없애는 것은 확실히 코드 실행 시간에 영향을 미친다
            # q에 삽입될 대상 후보군의 양 만큼 if 연산을 해야 하기 때문이다.
            # and data[nx][ny]==0:
            # 길인 경우만 이동가능 X : -> 벽인 경우는 이동 불가능
            # if 0<=nx<100 and 0<=ny<100 and not visited[nx][ny] and data[nx][ny]!=1:
            if data[nx][ny] != 1:
                if data[nx][ny] == 3:
                    return 1  # 도착 성공했음을 반환한다.

                # 이번 조사는 출발지 1개, 도착지 1개.
                # 즉, 누구든 도착만 했으면 된 거이.ㅁ
                data[nx][ny] = 1
                queue.append((nx, ny))

    # 모든 경우에 대해서 모두 조사를 했음에도,
    # 즉, while이 끝났음에도 아직 함수가 안 끝나고 있네?
    # 위에서 while안에서 return을 만적이 없어서 여기까지 왔다는 거네?
    return 0  # 아, 모든 경우에도 도착점 못 갔구나.


# _ 를 사용하는 경우가 있는데,
# for문으로 10번 반복 할건데, 그대 정의한 임시변수를
# 이 for문 안에서 사용하지 않을 때, 이렇게 작성
# 단, 메머리나 시간이나 그런거에 더 빨라지거나 그런 거 없다.
for _ in range(10):
    tc = int(input())
    data = [list(map(int, input())) for _ in range(100)]
    # 1: 벽, 0: 길, 2: 출발점, 3: 도착점.
    result = 0  # 도착지에 도착할 수 있는지 정보
    # BFS로 그래프를 탐색할 건데, 시작 정점이 어디인지 모르는 상황
    # -> BFS를 정의할 때, 시작 정점의 좌푯값을 넘겨 받을 수 있도록 만들어주자.
    # 시작 정점이 어딘지 찾아 나가야 한다.
    for x in range(100):
        for y in range(100):
            if data[x][y] == 2:  # 출발지라면
                # 약속, 조사 도중, 도착지에 도달하면 True 반환해주기
                result = search(x, y)  # 해당 위치에서 출발
                # 밑의 break는 본인이 속해있는 for문에 대해서만 정지
                break  # 출발지가 하나밖에 없으니 한번 조사했으면 끝.
        if result:  # 만약, 목적지에 도착했다면, result를 1로 바꿀 것
            break  # 그렇게 어떤 경우든 result가 1이 되면 break
    print(result)
    '''
    조사의 상황을 상하좌우 중 어디를 먼저 할 것인지를 if 문으로 달 수 있고 
    이것이 바로 백트래킹의 개념이다. 
    BFS 는 최단 경로를 얻을 수 있다. 해당 목적지를 갈 수 있는 길인지를 확인하기 
    위해서 모든 가능한 경로를 가기 때문에 오래 걸릴 수는 있으나 도착하는 시점에
    종료가 된다. 
    '''

