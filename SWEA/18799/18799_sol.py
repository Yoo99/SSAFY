import sys
sys.stdin = open("18799_input.txt")

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    if n==1:
        print(f"#{test_case} {sum(arr)}")
        continue
    else:
        subsets = []
        for i in range(1<<n):
            subset = []
            for j in range(n):
                if i & (1<<j):
                    subset.append(arr[j])
            subsets.append(subset)
        total_avg = 0
        for idx in range(1, len(subsets)):
            length = len(subsets[idx])
            avg = sum(subsets[idx])/length
            total_avg += avg
        total_avg = total_avg/(len(subsets)-1)
        if total_avg %1 ==0:
            ans = int(total_avg)
        else:
            ans = "{:.20f}".format(total_avg)
        print(f"#{test_case} {ans}")