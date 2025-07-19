
path = [] # 뽑은 카드들을 저장
def recur(cnt):
    # 카드를 2개 뽑으면 종료
    if cnt ==2:
        # 종료 시에 해야할 로직들을 작성
        print(*path)
        return
    # 1. 1개의 카드를 뽑는다
    path.append(0)
    # 2. 다음 재귀 호출을 한다 (뽑은 카드가 1개 추가되었다)
    recur(cnt+1)

    path.append(1)
    recur(cnt+1)

    path.append(2)
    recur(cnt+1)

# 제일 처음 호출할 때 시점이므로
#