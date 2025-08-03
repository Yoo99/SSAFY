import sys
sys.stdin = open("input.txt")

n = int(input())
array = list(map(int ,input().split()))
i, j,k = map(int, input().split())
for idx in range(i, j+1):
    array[idx] *=k
print(sum(array))