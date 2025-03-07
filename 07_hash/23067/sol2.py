import sys
sys.stdin = open("23067_input.txt")

T = int(input())

for test_case in range(1, T + 1):
    print("test_case", test_case)
    P, A, B = map(int, input().split())

    # 초기 탐색 값
    c = (1 + P) // 2
    ca, cb = c, c

    # 초기 정답 체크
    if ca == A and cb != B:
        print(f"#{test_case} A")
        continue
    elif cb == B and ca != A:
        print(f"#{test_case} B")
        continue
    elif cb == B and ca == A:
        print(f"#{test_case} 0")
        continue

    # 이진 탐색 초기 설정
    left_a, right_a = (ca, P) if ca < A else (1, ca)
    left_b, right_b = (cb, P) if cb < B else (1, cb)

    ca_list, cb_list = [ca], [cb]
    i = 0  # 반복 횟수 카운트

    while i < 1000:
        print(f"Iteration {i}: ca={ca_list[-1]}, cb={cb_list[-1]}")

        # 중간값 업데이트
        ca = (left_a + right_a) // 2
        cb = (left_b + right_b) // 2

        # 새로운 값 추가
        ca_list.append(ca)
        cb_list.append(cb)

        # A에 대한 이진 탐색 갱신
        if ca < A:
            left_a = ca + 1  # ✅ 경계 조정
        elif ca > A:
            right_a = ca - 1  # ✅ 경계 조정

        # B에 대한 이진 탐색 갱신
        if cb < B:
            left_b = cb + 1
        elif cb > B:
            right_b = cb - 1

        # 종료 조건
        if ca == A and cb == B:  # ✅ 목표값을 찾았을 때 종료
            break
        elif left_a >= right_a and left_b >= right_b:  # ✅ 이진 탐색 종료 조건
            break

        i += 1  # 반복 횟수 증가

    # 최종 비교 후 결과 출력
    if ca == A and cb != B:
        print(f"#{test_case} A")
    elif ca != A and cb == B:
        print(f"#{test_case} B")
    else:
        print(f"#{test_case} 0")
