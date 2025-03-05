def selection_sort(arr):
    n = len(arr)  # 배열의 길이
    # 처음부터 마지막 -1 번째까지 순회
    for i in range(n-1):
        min_idx = i # 현재 위치를 최소 위치로 설정

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx] , arr[i]



arr = [64, 25, 10, 22, 11]
selection_sort(arr)
print(arr)  # [10, 11, 22, 25, 64]
