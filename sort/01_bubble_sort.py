def bubble_sort(arr):
    n = len(arr)  # 배열의 길이
    # 아래 코드 작성
    for idx in range(n): # 처음부터 끝가지 순회
        for j in range(0, n-idx-1): # 0~~ 마지막 요소 1을 뺀다
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]



arr = [55, 7, 78, 12, 42]
bubble_sort(arr)
print(arr)  # [7, 12, 42, 55, 78]