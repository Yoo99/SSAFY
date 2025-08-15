import sys
sys.stdin = open("input.txt")

arr = list(input())
arr.sort()
print(''.join(arr))