def search(coins, amount):
    coins.sort(reverse =True)
    result= [{}]
    # 완전 탐색을 한다 -> 모든 경우의 수에 대해서 탐색을 하겠다
    # 조합
    # 최대한 적은 수의 동전을 사용해서 해결해야 한다
    min_coins = float('inf')
    def backtrack(remaining, index, current_comb, current_count):
        # nonlocal min_coins
        # 기저 조건 : 남은 금액이 0원이 된 경우
        if remaining == 0:
            # 현재 누적된 코인 <= min_coins
            # if current_count < min_coins:
            #     min_coins = current_count
            if current_count < min_coins[0]:
                min_coins[0] = current_count
                result[0] = current_comb.copy()
            return
        # 가지치기 : 현재 사용한 동전 수가, 지금까지 조사해서 얻어낸
        # 최소 동전 사용횟수보다 많으면 더 조사할 의미가 있을까?
        if current_count >= min_coins[0]:
            return

        # 아직 처리해야 할 금액이 남았다.
        for i in range(index, len(coins)):
            coin = coins[i]
            if coin <= remaining:
                # 현재 동전을 최대한 사용한다.
                max_count = remaining //coin
                for count in range(max_count, 0, -1):
                    current_comb[coin] = count
                    backtrack(remaining - coin*count, i+1, current_comb,current_count+count)
                    del current_comb[coin]
    backtrack(amount, 0, {}, 0)
    return result[0]



coins = [1,5, 10, 50, 100, 500]
amount = 482
result = search(coins, amount)

for coin, count in result.items():
    print(f'{coin}원: {count}개')