import sys
sys.stdin = open("input.txt")

n,m = map(int ,input().split()) # 배열의 크기, 질의의 개수
arr=  list(map(int, input().split()))
for _ in range(m):
    d=  int(input())
    cnt = 0
    for ele in arr:
        if ele>=d:
            cnt +=1
    print(cnt)