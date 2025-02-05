import sys
from itertools import combinations

sys.stdin = open("1486_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    # N: 사람 수, B: 선반의 높이
    N,B = map(int, input().split())
    # 점원들의 키 높이
    arr = list(map(int, input().split()))
    # 최종 결괏값 -> 우리는 B를 넘는 값 중 제일 낮은 값
    # 아래는 너무 큰 값 => 메모리랑 속도 신경쓰면서 기본값을 엄청 큰 값
    # result =float('inf')# 충분히 큰 값
    result = 10000 * 20 +1

    for r in range(1, N + 1):  # 1명부터 N명까지 선택
        # 전체 배열 arr명에서 r명 선택한 조합
        for comb in combinations(arr, r):
            total_height = sum(comb)
            if total_height >= B:
                # 그렇게 얻은 B보다 큰 값중, 제일 작은 값
                result = min(total_height, result)
    print(f"#{test_case} {result - B}")