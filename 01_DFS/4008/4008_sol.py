import sys
sys.stdin = open("4008_input.txt")

from itertools import permutations

mul_type=  ["+","-","*","/"]
# DFS를 푸는 방법
def unique_permutations(mul_list):
    seen = set()
    for p in permutations(mul_list):
        if p not in seen:
            seen.add(p)
            yield p

T = int(input()) # 테스트 케이스의 수
for test_case in range(1, T+1):
    N = int(input()) # 숫자의 개수
    stack = []
    result_list = []
    mul_list = list(map(int, input().split()))
    mul = list(zip(mul_list, mul_type))
    num = list(map(int, input().split()))
    mul_list=[]
    for b in mul:
        n, m = b
        line = [m for _ in range(n)]
        mul_list.extend(line)
    # print(mul_list)
    perm_mul = list(unique_permutations(mul_list))
    # print(perm_mul)
    for cal_list in perm_mul:
        stack.append(num[0])
        for i in range(0, len(cal_list)):
            num1 = stack.pop(0)
            num2 = num[i+1]
            cal_method = cal_list[i]
            if cal_method =="+":
                result = num1+num2
            elif cal_method =="*":
                result = num1*num2
            elif cal_method =="/":
                result = num1/num2
            elif cal_method =="-":
                result = num1-num2
            stack.append(int(result))
        result_list.append(stack[0])
        stack = []
    print(f"#{test_case} {max(result_list) - min(result_list)}")