arr = ['A','B','C','D','E']
n = 3

path = []
# 5 명 중 3명을 뽑는 문제
def recur(cnt, start):
    #
    if cnt == n:
        print(*path)
        return

    # 5명을 고려해야 한다.
    # 이전에 뽑았던 인덱스 +1 부터
    for i in range(len(arr)):
        path.append(arr[i])
        # i : i번째를 뽑겠다
        # 다음 재귀 부터는 i+1부터 고려해라
        recur(cnt +1, i+1)
        path.pop()


recur(0, 0)