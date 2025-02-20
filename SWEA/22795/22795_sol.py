import sys
sys.stdin = open("22795_input.txt")

T = int(input()) # 테스트 케이스의 수
for i in range(1, T+1):
    height = list(map(int, input().split()))
    sum_height = sum(height)
    x = max(height)+1
    while (sum_height+x) % (len(height)+1) !=0:
        x +=1
    print(x)
