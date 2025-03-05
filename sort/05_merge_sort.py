# 나누는 파트
def merge_sort(arr):
    n = len(arr)
    if n<=1:
        return arr
    mid = n//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # merge_sort(left_arr)
    # merge_sort(right_arr)

    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return merge(left, right)

# 합치는 파트
def merge(left, right):
    result = []  # 병합된 결과를 저장할 리스트

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # 왼쪽 배열의 남은 값을 모두 result에 삽입
    result.extend(left)
    result.extend(right)

    return result

arr = [69, 10, 30, 2, 16, 8, 31, 22]
result = merge_sort(arr)
print(result)  # [2, 8, 10, 16, 22, 30, 31, 69]
