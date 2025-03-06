import sys
sys.stdin = open("19003_input.txt")
from itertools import combinations, permutations, product


T = int(input())
for test_case in range(1, T+1):
    N , M = map(int ,input().split()) # N => 문자열의 개수, M => 각 문자열의 길이
    # 고른 문자열들을 적당히 재배열해서 순서대로 합쳤을 때, 팰린드롬이 되어야 함.
    arr = []
    for _ in range(N):
        string = input()
        arr.append(string)
    total_list = []
    for i in range(1, len(arr) +1):
        d = list(combinations(arr, i))
        for ele in d:
            print(ele)
            n = len(ele)
            bit = list(product([0,1], repeat = n))
            print(bit)