txt = input()

top = -1
stack = [0] * 100

ans = 1 # 짝이 맞다고 가정

for x in txt:
    if x=='(': # 여는 괄호 push
        top +=1
        stack[top] = x
    elif x ==')':
        if top==-1:
            ans = 0
            break
        top -=1
# 여는 괄호가 남아있으면
if top > -1:
    ans = 0
print(ans)