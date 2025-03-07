def fibo(n):
    global cnt
    cnt += 1
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

cnt = 0
print(fibo(10), cnt)

n = 10
# memoization code, 재귀 호출 중복을 방지해줌
cnt = 0
def fibo1(n):
    global cnt
    cnt += 1
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
print(fibo1(10), end = ' ')
print(cnt)