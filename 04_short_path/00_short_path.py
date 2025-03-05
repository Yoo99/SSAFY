import math

def short_path(vertex):
    # 시작 정점 'a'를 기준으로, b~f까지의 각 정점에
    # 도달하는데 드는 최소 비용을 조사하면서 갱신!
    # 이거 웬만하면 float('inf')보다 충분히 큰 값 찾아서 해라!
    # distances = {v: float('inf') for v in graph}
    distances = {v:math.inf for v in graph}
    print(distances)
    pass

graph = {
    'a':{'b':3, 'c':5},
    'b' :{'c':2,'d':6},
    'c':{'b':1, 'd':4, 'e':6},
    'd' :{'e':2, 'f':3},
    'e' : {'a':3, 'f':6},
    'f':{}
}

start_V = 'a'
result = short_path()