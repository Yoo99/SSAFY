'''
1. 분할 : 리스트의 길이가 1일 때까지 분할
2. 정복 : 리스트의 길이가 1이 되면 자동으로 정렬됨
3. 병합 :
    - 왼쪽, 오른쪽 리스트 중
    작은 원소부터 정답 리스트에 추가하면서 진행한다
'''

def merge_sort(arr):
    if len(arr)==1:
        return arr

    '''
    1. 절반 씩 분할
    '''
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    '''
    분할이 완료되면 병합되는 과정이 필요하다 
    '''
    return merge(left, right)
def merge(left, right):
    # 두 리스트를 병합한 결과 리스트
    result = [0] * (len(left) + len(right))
    l = r= 0
    while l<len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l +=1
        else:
            result[l+r] = right[r]
            r +=1
    # 두 리스트 중에 하나라도 남았다면
    # 왼쪽 리스트에 남은 애들을 모두 result에 추가
    while l <len(left):
        result[l+r] = left[l]
        l +=1
    # 오른쪽 리스트에 남은 애들 모두 result에 추가
    while r < len(right):
        result[l+r] = right[r]
        r+=1
    return result

arr = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_arr = merge_sort(arr)
print(sorted_arr)