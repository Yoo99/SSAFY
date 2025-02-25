import sys
sys.stdin = open("23048_input.txt")

T =int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        d= list(map(int, input().split()))
        arr.append(d)

    sorted_arr = sorted(arr, key = lambda x:x[1])
    cnt = 0
    d1 = sorted_arr.pop(0)
    end_time = d1[0]
    cnt +=1
    while sorted_arr:
        d2 =sorted_arr.pop(0)
        start_time = d2[0]
        if start_time>=end_time:
            cnt +=1
            end_time = d2[1]
        else:
            continue
    print(f"#{test_case} {cnt}")