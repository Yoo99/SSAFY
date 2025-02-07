import sys
import itertools
sys.stdin= open("5215_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, L = map(int, input().split())
    comb = []
    for i in range(N):
        T, K = map(int,input().split())
        arr = []
        arr = [T, K]
        comb.append(arr)
    total_list = []
    for r in range(1, len(comb)+1):
        total = list(itertools.combinations(comb,r))
        total_list.extend(total)
    taste = []
    max_taste = 0
    for ele in total_list:
        taste_sum, cal = 0, 0
        for b in range(len(ele)):
            taste_sum += ele[b][0]
            cal += ele[b][1]
        sum_cal = [taste_sum, cal]
        if cal<=L and taste_sum> max_taste:
            max_taste =taste_sum
        else:
            continue
    print(f"#{test_case} {max_taste}")
    # for i in range(len(taste)):
    #     if taste[i][1] <=L and taste[i][0]>max_taste:
    #         max_taste = taste[i][0]
    #     else:
    #         continue
    # print(f"#{test_case} {max_taste}")