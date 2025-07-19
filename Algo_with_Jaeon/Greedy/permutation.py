# [0,1,2] 3개의 카드가 존재
# 2개를 뽑을 예정

path = [] # 뽑은 카드들을 저장
# cnt = 재귀호출마다 누적되어서 전달되어야 하는 값
used = [False] * 7 # 1~ 6 숫자 사용 여부를 기록
# -> 그냥 0번 인덱스를 낭비하자!(편의를 위해)

# 조금 더 어려운 문제의 경우 (숫자 범위가 매우 크다)
# => 위와 같은 리스트 방식은 메모리 초과 가능성이 존재한다
# -<> dictionary(O(1)), set(O(1)) 이런 자료구조로 해결



def recur(cnt):
    # 카드를 2개 뽑으면 종료
    if cnt ==2:
        print(*path)
        return
    # 1. 1개의 카드를 뽑는다
    path.append(0)
    # 2. 다음 재귀 호출(뽑은 카드 1개 추가되었다)
    recur(cnt+1)
    path.pop()

    path.append(1)

    recur(cnt+1)
    path.pop()

    path.append(2)
    recur(cnt+1)
    path.pop()


def recur1(cnt):
    if cnt ==2:
        print(*path)
        return
    # 만약 카드가 1~ 6까지 6개가 있다면?
    for num in range(3):
        # 인덱스 검색 연산은 O(1)
        if used[num] is True:
            continue
        used[num] = True
        path.append(num)
        recur1(cnt+1)
        path.pop()
        used[num] = False
    return path
# 제일 처음 호출할 때 시점이므로
# 초기값을 전달하면서 시작
recur1(0)