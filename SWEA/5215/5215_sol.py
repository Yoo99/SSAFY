import sys
sys.stdin = open("5215_input.txt")

def recur(arr, add, suff, idx=0):
    print(arr, add, suff,idx)
    if idx ==len(arr):
        print(add)
        return
    if sum(add)>=1000:
        return
    recur(arr,add+[arr[idx][1]], suff+[arr[idx][0]], idx+1)
    recur(arr, add,suff, idx+1)



T = int(input()) # test_case의 수
for test_case in range(1, T+1):
    food_list = []
    N, L = map(int, input().split())
    for _ in range(N):
        a,b =map(int,input().split())
        food_list.append((a,b))
    food_list.sort(reverse=True)
    print(food_list)
    max_cal = 0
    for idx in range(0, len(food_list)):
        total_cal = 0
        max_suff = 0
        arr = food_list[idx:]
        add = []
        suff = []
        recur(arr, add, suff,idx=0)
        print("add", add)
        # print("suff", suff)

