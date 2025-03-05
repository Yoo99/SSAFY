def counting_sort(arr, max_value):
    n = len(arr)  # 배열의 길이
    counts = [0] * (max_value +1) # 충분히 큰 공간으로 만들어주기
    # 졍렬 결과를 담을 배열
    result =  [0] * n

    # 각 원소의 등장 횟수를 작성
    for num in arr:
        counts[num] +=1

    for i in range(1, max_value+1):
        counts[i] += counts[i-1]

    for num in reversed(arr):
        result[counts[num] - 1 ] = num
        counts[num] -= 1
    return result


arr = [0, 4, 1, 3, 1, 2, 4, 1]
result = counting_sort(arr, 4)
print(result)  # [0, 1, 1, 1, 2, 3, 4, 4]