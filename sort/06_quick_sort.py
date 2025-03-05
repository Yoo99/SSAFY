# 분할하는 파트
def quick_sort(arr, start, end):
    if start < end:
        # 피벗을 기준으로 리스트를 분해하고 정렬
        pivot = partition(arr, start, end)

        quick_sort(arr, start, pivot -1) # 왼쪽
        quick_sort(arr, pivot+1, end) # 오른쪽


# 분할된 영역을 정렬하는 파트
def partition(arr, start, end):
    pivot = arr[start]
    left = start +1
    right = end

    while True:
        # left가 할 일 : pivot 보다 크거나 같은 값을 찾는다.
        while left <= end and arr[left] < pivot:
            left += 1
        while right > start and arr[right] >= pivot:
            right -= 1
        # left와 right가 아직 교차하지 않았다면
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break
    arr[start], arr[right] = arr[right], arr[start]
    return right


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
# 처음 인덱스를 피벗으로 설정해서 퀵 정렬 시작
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
