import sys
sys.stdin = open("1486_input.txt", "r")


def combination(arr, r):
    acc = [] # 누적 결괏값을 넣을 배열
    if r==1: # 선택할 요소의 수가 1인 경우 # 더 이상 선택할 게 없는 경우
        return [[i] for i in arr]
    # 배열에 대해서 반복할 것
    for i in range(len(arr)):
        elem = arr[i] # 현재 요소를 선택
        for rest in combination(arr[i+1:], r-1):
            acc.append([elem] + rest)
    return acc



T = int(input())
for test_case in range(1, T+1):
    # N: 사람 수, B: 선반의 높이
    N,B = map(int, input().split())
    # 점원들의 키 높이
    arr = list(map(int, input().split()))
    # 최종 결괏값 -> 우리는 B를 넘는 값 중 제일 낮은 값
    # 아래는 너무 큰 값 => 메모리랑 속도 신경쓰면서 기본값을 엄청 큰 값
    # result =float('inf')# 충분히 큰 값 => B를 넘는 값중 제일 낮은 값을 가지고 올 것이기 때문이다.
    result = 10000 * 20 +1 # 문제에서 제일 큰 사람의 키가 10000이라고 주어졌기 때문이다.

    # 완전 검색 => 전부 조회할 것.
    for r in range(1, N+1): # 1명부터 N명까지 선택
        # 전체 배열 arr명에서 r명 선택한 조합
        for comb in combination(arr, r):
            total_height = sum(comb)
            if total_height>= B: # 선반보다는 높아야 함
                # 그렇게 얻은 B보다 큰 값중, 제일 작은 값
                result = min(total_height, result)
    print(f"#{test_case} {result-B}")