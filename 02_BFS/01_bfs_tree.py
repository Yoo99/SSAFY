from collections import deque
# 앞으로 Q를 구현해야 한다면 deque 씁시다.

# DFS -> STACK , BFS -> QUEUE
def BFS(node_index):
    # q가 존재하는 동안 조사를 진행할 예정이다. -> Q를 생성
    queue = deque([node_index])
    # 이 함수가 반환할 최종 결괏값
    result = []
    while queue:
        # Q가 가진 첫번째 원소를 반환
        now_idx = queue.popleft()
        result.append(now_idx)
        # 현재노드가 가진 모든 자식들에 대해서 조사를 진행해야 한다
        for child_idx in tree[now_idx][1:]:#  슬라이싱은 범주를 벗어나서 반환할게 없어져도 빈 리스트를 반환하게 된다.
            queue.append(child_idx)
    return result
# 트리정보
# 0번 인덱스를 사용할 것인지 정하자.
# 각 노드가 가지고 있을 값이 중요하다면?
# 자식 노드들의 정보는 어떻게 표현할 것이냐?
tree = [None,
        # 0번 -> 노드의 값
        # 1번 이후 -> 자식의 index를 삽입
        ['A', 2,3,4], # 1번 인덱스
        ['B', 5,6], # 2번 인덱스
        ['C'],
        ['D',7,8,9],
        ['E'] , ['F'], ['G'], ['H'], ['I']
        ]
result = BFS(1) # root 노드의 인덱스 부터 조사를 시작
for idx in result:
    print(tree[idx][0])