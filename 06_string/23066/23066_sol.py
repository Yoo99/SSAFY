import sys
sys.stdin = open("23066_input.txt")

T = int(input())
for test_case in range(1, T+1):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))
    sum_list = []
    for i in str1:
        count  = 0
        count = str2.count(i)
        sum_list.append(count)

    print(f"#{test_case} {max(sum_list)}")