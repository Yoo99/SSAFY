import sys
sys.stdin =open("22039_input.txt")
from itertools import combinations

def fibonacci(N):
    arr= []
    for i in range(0,N):
        if i == 0:
            arr.append(1)
        elif i == 1:
            arr.append(1)
        elif i>1:
            arr.append(arr[-1] + arr[-2])
    return arr

# def generate_subsets(arr):
#     n = len(arr)
#     subsets = []
#     pair_sets = []
#     for i in range(1 << n):
#         subset = []
#         for j in range(n):
#             if i & (1<<j):
#                 subset.append(arr[j])
#         subsets.append(subset)
#         subarr = arr.copy()
#         for b in subset:
#             subarr.remove(b)
#         pair_sets.append(subarr)
#     return subsets, pair_sets


T = int(input())
for test_case in range(1, T+1):
    N  = int(input())
    arr = fibonacci(N)
    mid = sum(arr)//2
    ans = "impossible"
    if mid <1 or sum(arr)%2!=0:
        print(ans)
        continue
    generate_subsets = []
    for i in range(len(arr)+1):
        d = list(combinations(arr, i))
        generate_subsets.extend(d)
    ans_list = []
    for d in generate_subsets:
        if sum(d) == mid:
            ans_list += ["B"] * len(d)
            ans_list += ["A"] * (len(arr) - len(d))
            print(''.join(ans_list))
            break
        # else:
        #     print(ans)

    # subsets, pair_sets = generate_subsets(arr)
    # for idx in range(0, len(subsets)):
    #     if sum(subsets[idx]) == sum(pair_sets[idx]) == mid:
    #         ans_list = []
    #         ans_list += ["B"]*(len(subsets[idx]))
    #         ans_list += ["A"]*(len(pair_sets[idx]))
    #         print("".join(ans_list))
    #         break








