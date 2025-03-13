# cnt = 재귀호출마다 누적되어서 전달되어야 하는 값
path =[]
used = [False] * 7  # 숫자 사용 여부 기록
def recur(cnt,path):
    # 카드를 2개 뽑으면 종료
    if cnt ==2:
        # 종료 시에 해야할 로직들을 작성
        print(*path)
        return
    # 1. 1개의 카드를 뽑는다
    # 2. 다음 재귀 호출 (뽑은 카드가 1개 추가되었다)
    # path.append(0)
    # recur(cnt+1)
    # path.pop()
    #
    # path.append(1)
    # recur(cnt+1)
    # path.pop()
    #
    #
    # path.append(2)
    # recur(cnt+1)
    # path.pop()
    # 카드 0~2
    for num in range(6):
        # 중복을 허용하지 않는 경우:
        if used[num] is True: # 하지만 이러한 경우에는 시간초과가 날 것이다
            continue
        used[num] = True
        path.append(num)
        recur(cnt+1, path)
        path.pop()
        used[num] = False

# 제일 처음 호출할 때 시점이므로
# 초기값을 전달하면서 시작
recur(0, path)



