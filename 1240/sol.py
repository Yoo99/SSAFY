import sys

sys.stdin = open('input.txt', 'r')

num = {0:'0001101',1:'0011001',2:'0010011', 3:'0111101',4:'0100011',5:'0110001',6:'0101111', 7:'0111011',8:'0110111',9:'0001011'}

tc = int(input())

for test_case in range(1, tc+1):
    N,M = map(int, input().split())
    arr = []
    for i in range(N):
        line = list(input())
        set_line = set(line)
        if len(set_line)==1:
            continue
        else:
            arr.append(line)
    arr_list = arr[0]
    arr_list.reverse()
    for i in arr_list:
        if i == 0:
            arr_list.remove(i)
        else:
            break
    arr_list = arr_list[:56]
    arr_list.reverse()
    print(arr_list)
