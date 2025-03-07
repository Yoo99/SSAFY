import sys
import math
sys.stdin = open("5688_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    d = round(math.pow(N, 1/3))
    if d**3 == N:
        print(f"#{test_case} {int(d)}")
    else:
        print(f"#{test_case} -1")