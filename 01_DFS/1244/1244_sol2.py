import sys
import itertools
sys.stdin = open("1244_input.txt", "r")

tc = int(input())
for test_case in range(1, tc+1):
    num , cnt = map(int, input().split())
    num_list = list(str(num))
    # print(num_list)
    len_num = list(str(num))
    temp = [str(num)]
    # 인덱스를 담을 리스트 ans
    ans = [i for i in range(len(len_num))]
    #위치 조합을 구하기 _ 인덱스 기준으로 (따라서 permutation의 대상은 ans이다
    # 위치조합_case 리스트에 받기
    case = list(itertools.permutations(ans, 2))
    for _ in range(cnt):
        temp_2 = []
        for i,j in case:
            for e in temp:
                list_e = list(e)
                list_e[i], list_e[j] = list_e[j], list_e[i]
                e = ''.join(list_e)
                temp_2.append(e)
        temp = list(set(temp_2))
    print(f"#{test_case} {max(temp)}")
