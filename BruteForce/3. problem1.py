# 카드 5장을 뽑아라
# 5장을 뽑았을 때, 연속된 3개가 나오면 counting을 하라

'''
1. 전체를 보라
2. 끝날 때 무언가 하라
3. 중복을 제거하라
'''

card = ['A','J','Q','K']
path = []
result = 0

def count_three():
    for i in range(0, 5-2):
        if path[i] == path[i+1] == path[i+2]:
            return True
    return False

def recur(cnt):
    global result
    if cnt == 5:
        # 연속된 3개가 나오면 counting을 하라
        if count_three():
            result +=1
            print(path)
        return

    for idx in range(4):
        path.append(card[idx])
        recur(cnt+1)
        path.pop()
recur(0)