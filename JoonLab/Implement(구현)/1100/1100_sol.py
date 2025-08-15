import sys
sys.stdin = open("input.txt")

arr = input().strip()
n = int(input())
while len(arr)<n:
    arr += arr[-1]
    if len(arr)==n:
        break
print(arr)