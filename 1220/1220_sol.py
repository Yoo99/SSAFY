import sys
sys.stdin = open("1220_input.txt", "r")

n = int(input())
arr = []
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)
for col in range(1):
    for row in range(n):
        if arr[row][col] == 0:
            continue
        elif arr[row][col] == 1:
            while 0<=row-2<n and arr[row-2][col] != 2:
                arr[row][col] = 0; arr[row-1]



#
# for test_case in range(1, 11):
#     n = int(input())
#     arr = []
#     for i in range(n):
#         line = list(map(int, input().split()))
#         arr.append(line)
#     for row in arr:
#         print(row)