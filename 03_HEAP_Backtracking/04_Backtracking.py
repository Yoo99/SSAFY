

def find_subset(start, current_subset, current_sum):
    # print(current_subset, start)
    if len(current_subset) == R:
        if current_sum == target_num:
            result.append(current_subset[:])

        return
    # 일단 완전 탐색을 해
    # 현재 선택할 대상 idx 부터 마지막 요소까지

    # 가지치기
    if current_sum>target_num:
        return
    print(current_subset, start)

    for i in range(start, len(numbers)):
        selected_num = numbers[i]
        # 현재 수를 선택 => 현재 부분집합에 해당 요소를 삽입.
        current_subset.append(selected_num)
        # 선택한 요소와 함께 다음요소를 선택하러 떠난다.
        find_subset(i+1, current_subset, current_sum+selected_num)   # 현재 요소 다음 요소부터 선택하도록
        # 현재 요소를 선택했었던 일을 없었던 것으로 하고, 다음 i번째 요소를 선택
        current_subset.pop()
numbers = list(range(1, 11))
# print(numbers)
target_num = 15  # 5개 선택해서 그 합이 15인 경우,

R = 5
result = []
# DFS로 진행 할때 필요한 파라미터
# 1. 재귀를 중단 시킬 파라미터가 필요 -> 5개를 모두 선택했다면 종료 (모든 선택지를 볼 필요가 없다)
# 2. 누적해서 가져가야 할 값들. -> 부분집합을 만드는 것이 목적
# 3. 현재 선택할 원소를 가리키는 idx 필요

find_subset(start = 0, current_subset = [], current_sum = 0)
