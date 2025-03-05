import sys
sys.stdin = open("23061_input.txt")

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)

        quick_sort(arr, start, pivot -1)
        quick_sort(arr, pivot+1, end)

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end

    while True:
        while left <= end and arr[left] < pivot:
            left += 1
        while right > start and arr[right] >= pivot:
            right -=1
        if left < right :
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break
    arr[start], arr[right] = arr[right], arr[start]
    return right


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr)-1)
    print(f"#{test_case} {arr}")