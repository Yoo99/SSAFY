import sys
sys.stdin = open("15649_input.txt")

def recursion(arr):
    if len(arr) == M:
        print(*arr)
        return arr
    # print(arr)
    for i in range(1, N+1):
        if i in arr:
            continue
        recursion(arr + [i])


while True:
    try:
        N, M = map(int,input().split())
        # 반복해야 하는 숫자 N, 출력 길이 M
        recursion([])
    except:
        break