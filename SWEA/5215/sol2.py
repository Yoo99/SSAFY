import sys
sys.stdin = open("5215_input.txt")

def recur(stack,suff,start):
    global suff_list
    if start== len(food_list):
        return
    if sum(stack)>1000:
        return
    recur(stack, suff,start+1)
    suff.append(food_list[start][0])
    stack.append(food_list[start][1])
    if sum(stack)<=1000:
        recur(stack,suff, start+1)
    stack.pop()


    # return max_sum

T = int(input())
for test_case in range(1, T+1):
    N, L = map(int, input().split())
    food_list = []
    for _ in range(N):
        a,b = map(int, input().split())
        food_list.append((a,b))
    food_list.sort(reverse= True)
    print("food_list", food_list)
    suff_list = []
    recur([],[],0)
    print(suff_list)