import sys
sys.stdin = open("input.txt")

money =int(input()) # 현금
price = list(map(int, input().split())) # 가격
# 성민이
def time(money, price):
    stock, up, down = 0, 0, 0
    for idx in range(1, len(price)):
        if price[idx] > price[idx-1]:
            up +=1
            down = 0
        elif price[idx] < price[idx-1]:
            up = 0
            down +=1
        else:
            up, down = 0,0
        if up ==3:
            money += stock * price[idx]
            stock = 0
            up = 0
        elif down >=3:
            stock += money//price[idx]
            money %= price[idx]
            down = 0
    money += stock*(price[-1])
    return money
# 준현이
def bnp(money, price):
    stock = 0
    for idx in range(len(price)):
        stock += money//price[idx]
        money %= price[idx]
    money += stock * price[-1]
    return money
bnp_m = bnp(money, price)
time_m = time(money, price)
if bnp_m == time_m:
    print("SAMESAME")
elif bnp_m> time_m:
    print("BNP")
else:
    print("TIMING")


