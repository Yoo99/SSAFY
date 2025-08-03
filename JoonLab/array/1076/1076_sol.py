import sys
sys.stdin=  open("input.txt")

string = list(input())
ans = ''
for b in range(len(string)):
    if b%2==1:
        ans += string[b]
print(ans)