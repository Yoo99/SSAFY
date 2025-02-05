import sys
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

    # 모든 경의 수 (공집합 제외하고 처리)
    # for i in range(1, 1<<N): # 1부터 1을 N번 만큼 shift해서 처리
    for i in range(1, 2**N):
        height = 0   # 높이를 더해나갈 변수
        for j in range(N): # 0번 부터 N번까지의 사람을 선택했는지 판별용
            # 각 부분 집합
            # i 번째 경우에서 j번째 요소가 선택되었는지를 판별
            if i & (1<<j):
                height += arr[j]
        # 모든 요소에 대해서 i번째 경우의 수를 다 구했다면
        if height>= B:
            result = min(height, result)
    print(f"#{test_case} {result - B}")