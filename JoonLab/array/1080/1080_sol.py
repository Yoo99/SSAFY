import sys
sys.stdin = open("input.txt")

string = list(input())
ans = ''
for e in string:
    ans += e.upper()

print(ans)