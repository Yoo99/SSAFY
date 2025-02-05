import sys
import itertools
sys.stdin = open("1244_input.txt", "r")

tc = int(input())
for test_case in range(1, tc+1):
    num , cnt = map(int, input().split())
    num_list = list(str(num))
    print(num_list)
    len_num = list(str(num))
    ans = [i for i in range(len(len_num))]
    case = list(itertools.permutations(ans,2))
    total_case = list(itertools.product(case, repeat = 2))
    result = []

    for b in total_case:
        for e in range(2):
            i, j = b[e]
            sub1, sub2 = 0, 0
            sub1 = num_list[i]; sub2 = num_list[j]
            num_list[i] = sub2
            num_list[j] = sub1
        result.append(''.join(num_list))
    print(set(result))