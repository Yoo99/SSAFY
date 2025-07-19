path = []
result = 0
def recur(cnt):
    global result
    if cnt == 3:
        print(path)
        if sum(path) <=10:
            result +=1
        return
    for num in range(1,7):
        path.append(num)
        recur(cnt+1)
        path.pop()
recur(0)
print(result)

def recur(cnt, total):
    global result
    # 이미 10을 넘으면 더 이상 볼 필요가 없다
    # 기저조건에서 경우의 수들을 많이 줄여주는 기법
    if total >10:
        return
    # if cnt == 3:
    #     # 합이 10 잏인 건 몇 개인가?
