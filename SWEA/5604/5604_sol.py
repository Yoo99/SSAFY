import sys
sys.stdin = open("5604_input.txt")

T = int(input())
for test_case in range(1, T+1):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B+1):
        i  =str(i)
        d= list(map(int, i))
        cnt +=sum(d)
    print(f"#{test_case} {cnt}")