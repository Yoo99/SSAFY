import sys
sys.stdin = open("input.txt")

arr = []
for _ in range(9):
    line=  list(map(int ,input().split()))
    arr.append(line)
max_num = [0, 0, 0] # 숫자, x, y
for idx in range(9):
    for idy in range(9):
        if arr[idx][idy] > max_num[0]:
            max_num = [arr[idx][idy], idx,idy]

print(max_num[0])
print(max_num[1]+1, max_num[2]+1)