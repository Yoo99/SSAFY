'''
중복 제거 순열
'''

path = [] # 뽑은 카드들을 저장
used = [False] * 7 # 1~ 6 사용 여부를 기록

def recur(cnt):
    if cnt ==3:
        print(*path)
        return
    for num in range(1, 7):
        # 이미 num을 뽑았다면 뽑지 마라
        # == num을 뽑지 않았을 때만 뽑아라
        # in : path를 전체 검사하게 되기 때문에 비효율

        # 인덱스 검색 연산은 O(1) 
        if used[num] is True:
            continue
        used[num] = True
        path.append(num)
        recur(cnt+1)
        path.pop()
        used[num] = False
recur(0)