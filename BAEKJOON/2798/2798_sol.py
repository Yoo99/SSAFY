import sys
sys.stdin = open("input.txt")

N, M=  map(int, input().split())
numbers = list(map(int, input().split()))
used = [] # 지금까지 수집한 카드 리스트
max_result = 0
sub = [] # 부분집합 넣을 곳
def find(cnt):
    global max_result
    if cnt ==3:
        if sum(sub)> max_result and sum(sub)<=M:
            max_result = sum(sub)
        return
    for num in numbers:
        if num not in used:
            sub.append(num)
            used.append(num)
            find(cnt+1)
            used.remove(num)
            sub.pop()

find(0)
print(max_result)