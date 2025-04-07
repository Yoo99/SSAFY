import sys
sys.stdin = open("17103_input.txt")

is_prime=[True] * (1000001)
is_prime[0], is_prime[1] = False, False
for i in range(2, 1000001):
    for j in range(i*i, 1000001, i):
        if is_prime[j]:
            is_prime[j] = False

T = int(input()) # test_case의 개수
for _ in range(T):
    n = int(input())
    cnt = 0
    for i in range(2, n//2+1):
        if is_prime[i] and is_prime[n-i]:
            cnt+=1
    print(cnt)
