import sys
import itertools
sys.stdin = open("1244_input.txt", "r")

tc = int(input())
for test_case in range(1, tc+1):
    num , cnt = map(int, input().split())
    num_list = list(str(num))
    # print(num_list)
    len_num = list(str(num))
    # 인덱스를 담을 리스트 ans
    ans = [i for i in range(len(len_num))]
    #위치 조합을 구하기 _ 인덱스 기준으로 (따라서 permutation의 대상은 ans이다
    # 위치조합_case 리스트에 받기
    case = list(itertools.permutations(ans,2))
    # 위치조합을 중복순열로 cnt개씩 선택한 경우를 구하기 _ test_case
    if cnt == 1:
        test_case = case
    else:
        test_case = list(itertools.product(case,repeat = cnt))
    print(test_case)