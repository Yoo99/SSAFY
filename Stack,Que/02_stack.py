def check(expression):
    stack = [] # 여는 괄호를 쌓을 스택
    for char in expression:
        if char == "(" :     # 여는 괄호면 일단 stack에  append)
            stack.append(char)
        elif char == ")": # 닫는 소괄호면,
            # stack이 비었거나 여는 소괄호가 아니라면 false
            if not stack or stack[-1] !="(":
                return False
            stack.pop()
            # 비어있는 list -> False -> not []
    # 모든 조사를 마쳤는데 stack이 비었다 -> 올바른 괄호다
    # 모든 조사를 마쳤는데 stack이 비지 않았다 -> 틀림
    return not stack
examples ='if ((i ==0 && (j==0)'
print(check(examples))