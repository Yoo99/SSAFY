import sys
sys.stdin = open("input.txt")

string = list(input())
chars = list(map(str, input().split()))

ans = ''
for e in string:
    if e in chars:
        ans += e.lower()
    else:
        ans += e
print(ans)