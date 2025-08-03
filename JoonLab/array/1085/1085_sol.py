import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
dict = {}
for _ in range(n):
    key ,value=  map(str, input().split())
    dict[key] = int(value)
shop = list(map(str, input().split()))
total = 0
for ele in shop:
    total += dict[ele]
print(total)