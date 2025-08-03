import sys
sys.stdin=  open("input.txt")

a_string = set(list(map(str, input().split())))
b_string =set(map(str, input().split()))
ans = []
for ele in a_string:
    if ele not in b_string:
        ans.append(ele)
ans.sort()
for b in ans:
    print(b)

