# 트리 정보를 삽입한다.
# 0번 인덱스를 사용할 것인지 정하자.
# 0번 노드를 사용하지 않을 예정이라면 0 또는 None 을 넣어두자.
# 자식 노드들의 정보는 어떻게 표현할 것이냐?
from collections import deque
# 앞으로 Q를 구현해야 한다면 deque를 씁시다.
def BFS(node_index):
    # q가 존재하는 동안. -> Q를 생성해야 한다.
    queue = deque([node_index])
    # 이 함수가 반환할 최종 결괏값
    result = []
    while queue:
        # Q가 가진 첫번째 원소를 반환해준다
        now_idx = queue.popleft()
        result.append(now_idx)
        # 현재 노드가 가진 모든 자식들에 대해서 조사를 시작한다.
        for child_idx in tree[now_idx][1:]: # 만약에 리스트 인덱스가 0밖에 없는 경우라면 어차피 빈 리스트를 반환
            queue.append(child_idx)  #child_idx가 없다면 for문이 알아서 끝날 것임
    return result
tree = [None,
# 0번 ->노드의 값
# 1번 이후 -> 자식의 index
 ['A', 2,3,4], # 1번 인덱스
    ['B', 5,6] , # 2번 인덱스
    ['C'] ,
    ['D', 7,8,9],
    ['E'], ['F'], ['G'], ['H'], ['I'] # 자식이 없는 노드들도 마찬가지로 리스트에 담아서 적어두기
 ]
result = BFS(1) # root 노드의 인덱스  # 0번 인덱스가 없기 때문에 1번 노드부터 탐색을 시작할 예정이다
print(result)
for idx in result:
    print(tree[idx][0], end = " ")