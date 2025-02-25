coins = [1,5, 10, 50, 100, 500]
amount = 482
result = {}

def search(coins, amount):
    '''
    그리디한 방식으로 거스름돈 해결하기
    가장 큰 동전으로 우선 거슬러주고, 나머지는 다시 작은 돈으로 거슬러 주기.
    위를 충족하기 위해서는 ... 동전의 종류를 내림차순 `정렬`해주면 된다
    '''
    coins.sort(reverse = True) # 내림차순 정렬
    '''
    amount가 coin보다 클 동안 계속 빼거나 나누어야 하기 때문에 
    while문을 써도 될 듯 
    '''
    result = {}
    for coin in coins:
        if amount>=coin:
            count = amount//coin
            amount = amount % coin
            result[coin] = count
    return result

result = search(coins, amount)

for coin, count in result.items():
    print(f'{coin}원: {count}개')