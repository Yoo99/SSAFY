import sys
sys.stdin=open("10726_input.txt", "r")
tc = int(input())
for test_case in range(1, tc+1):
    N,M = map(int,input().split())
    arr = []
    d= bin(M)
    arr = list(map(int, d[2:]))
    ans = ""
    if len(arr)>=N and set(arr[-N:])=={1}:
        ans = "ON"
    else:
        ans = "OFF"
    print(f"#{test_case} {ans}")