import sys
sys.stdin = open("5607_input.txt")
from math import factorial


T = int(input())
for test_case in range(1, T+1):
    N, R = map(int, input().split())
    if (N-R)<R:
        R = N-R
    ans = factorial(N)//(factorial(R) * factorial(N-R))
    if ans < 1234567891:
        print(f"#{test_case} {ans}")
        continue
    ans %= 1234567891
    print(f"#{test_case} {ans}")