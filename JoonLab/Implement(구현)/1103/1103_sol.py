import sys
sys.stdin = open("input.txt")

arr =list(input())
ans = []
is_A = False
while arr:
    d = arr.pop(0)
    if d !='a' and d!='A':
        ans.append(d)
        is_A= False
    else:
        if not is_A:
            ans.append(d)
            is_A =True
        else:
            ans = ans[:-1]
            ans += ['a']

print(''.join(ans))