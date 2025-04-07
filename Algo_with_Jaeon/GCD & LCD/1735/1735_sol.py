import sys
sys.stdin = open("1735_input.txt")

# 최대 공약수 구하기 -> 최소 공배수는 두 수의 곲을 최대 공약수로 나눈 몫이다
def GCD(n1, n2):
    d1, d2 = max(n1,n2), min(n1,n2)
    while d2>0:
        if d1%d2 == 0:
            return d2
        d1, d2 = d2, d1%d2
    return d1

while True:
    try:
        a,b = map(int,input().split())
        c,d = map(int, input().split())
        under = (b*d) //GCD(b,d)
        upper = a*(under//b) + c*(under//d)
        under_r = under//GCD(under, upper)
        upper_r = upper//GCD(under,upper)
        print(upper_r,under_r)
    except:
        break
