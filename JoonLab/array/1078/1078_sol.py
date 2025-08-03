import sys
sys.stdin = open("input.txt")

string = list(input())
ans = ''
for char in string:
    if char.isupper():
        continue
    else:
        ans += char
print(ans)
