def merge_sort(arr):
    # 1. 기저 조건 설정 (길이가 1 이하일 때에는 그대로 반환)
    global cnt
    cnt +=1
    if len(arr)<=1:
        return arr

    # 2. 중간 인덱스 찾기
    mid = len(arr) //2

    # 3. 왼쪽 / 오른쪽 반으로 나눠서 재귀 호출
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 4. 정렬된 두 부분을 병합한다
    return merge(left, right)

def merge(left, right):
    result = []
    i  = j = 0
    while i <len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j +=1
    result.extend(left[i:])
    result.extend(right[j:])

    return result
arr = [38, 27, 43, 3, 9, 82, 10]
cnt = 0
sorted_arr = merge_sort(arr)
print(sorted_arr)
print(cnt)