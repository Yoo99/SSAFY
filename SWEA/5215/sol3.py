import sys
sys.stdin = open("5215_input.txt")


def recur(idx, cur_cal, cur_suff):
    print(idx, cur_suff, cur_cal)
    global max_suff
    if cur_cal>1000:
        return
    if idx == len(food_list):
        max_suff = max(cur_suff, max_suff)
        return

    recur(idx + 1, cur_cal, cur_suff)
    recur(idx+1, cur_cal+food_list[idx][1], cur_suff+food_list[idx][0])

T = int(input())
for test_case in range(1, T+1):
    N, L = map(int, input().split())
    food_list = []
    for _ in range(N):
        a,b = map(int,input().split())
        food_list.append((a,b))
    # food_list.sort(reverse = True)
    max_suff = 0
    recur(0, 0,0)
    print(max_suff)