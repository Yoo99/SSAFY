'''
주사위 3개를 던져 합이 10이하인 경우는 몇 개인가?
주사위는 1~6
종료조건 : 3번 던진다
나올 수 있는 범위 : 주사위는 1~6
'''

path = []
result = 0
def recur(cnt, total ):
    global result
    # 기저 조건 가지치기
    # 이미 10을 넘으면 더 이상 볼 필요가 없다.
    if total>10:
        return
    
    if cnt ==3:
        # 합이 10 이하인 건 몇 개인가
        if total <=10:
            result +=1
            print(path)
        return

    for num in range(1, 7):
        path.append(num)
        # 주사위 결과를 더해서 전달
        recur(cnt +1, total + num)
        path.pop()


recur(0,0)