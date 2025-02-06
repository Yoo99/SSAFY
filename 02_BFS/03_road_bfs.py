import sys
from collections import deque
sys.stdin = open("input.txt")

# 1.
def get_road_move_time():
    # q 가 필요함
    # (0, 0) -> (N-1, M-1)
#   queue = deque([(0,0)])



N, M = map(int, input().split()) # N, M이 가로인지 세로인지 반드시 확인할 것
data = [list(map(int, input())) for _ in range(N)]
print(data)
# 최종 결괏값
result = -1 # 문제에서 도달하지 못했을 때 반환하라고 하는 값을 넣으면 된다.
# 함수 이름을 DFS or BFS로 정의하는 것은 권장하지 않는다.
# 정확한 용도를 작성 해 달라.
# 함수의 역할 : 이동하는데 드는 최소 비용을 구하는 함수
# 이 문제에서는 출발 정점의 x,y 좌표가 고정이다 -> (0, 0)
get_road_move_time()   # 출발을 시작할 정점 정보
