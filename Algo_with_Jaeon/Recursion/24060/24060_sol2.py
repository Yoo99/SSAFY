import sys
sys.stdin = open("24060_input.txt")

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = (len(arr)+1)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i, j = 0,0
    while i< len(left) and j< len(right):
        if left[i] < right[j]:
            result.append(left[i])
            ans.append(left[i])
            i +=1
        else:
            result.append(right[j])
            ans.append(right[j])
            j +=1
    while i<len(left):
        result.append(left[i])
        ans.append(left[i])
        i +=1
    while j < len(right):
        result.append(right[j])
        ans.append(right[j])
        j+=1
    return result

while True:
    try:
        N, K = map(int, input().split())
        arr = list(map(int ,input().split()))
        ans = []
        cnt = 0
        d = merge_sort(arr)
        if len(ans)<K:
            print(-1)
        else:
            print(ans[K-1])
    except:
        break