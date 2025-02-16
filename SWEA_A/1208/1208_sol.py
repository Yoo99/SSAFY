import sys
sys.stdin = open("1208_input.txt","r")
for test_case in range(10):
    N = int(input())
    arr= list(map(int, input().split()))
    for i in range(N):
        max_height = max(arr)
        min_height = min(arr)
        max_idx = arr.index(max_height)
        min_idx = arr.index(min_height)
        max_height -= 1; min_height += 1
        arr[max_idx] = max_height
        arr[min_idx] = min_height

    diff = max(arr) - min(arr)
    print(f"#{test_case} {diff}")