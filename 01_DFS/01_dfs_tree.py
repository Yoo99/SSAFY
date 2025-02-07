# 트리를 인접 리스트 방식
# keyError 발생을 방지하기 위해서,
# 자식이 없는 경우, [] 할당하는 방법이 있을 수 있음

tree = {
    'A':['B','C','D'],
    'B': ['E','F'],
    'D': ['G','H','I']
}

# DFS 함수를 정의
#                노드의 index는 무엇인가?
# node: 현재 방문한 노드의 값이 무엇인가?
def dfs(node):
    # 현재 방문한 노드의 정보를 한 줄로 출력
    print(node, end = ' ')

    # 현재 노드가 가진 모든 자식들에 대해서 방문
    # for child in tree[node]:
    # dict.get() 메서드로 존재하지 않는 key 조회시, None 반환
    # 파이썬의 for문은 비어있는 iterable 객체를 순회하라고 하면
    # 코드를 실행하지 않음
    for child in tree.get(node, []):  #get이라는 메서드, 함수
        # 자식들 기준으로 재 방문
        print(child)
        dfs(child)

dfs('A')