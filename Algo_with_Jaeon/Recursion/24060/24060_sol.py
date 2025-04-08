import sys
sys.stdin = open("24060_input.txt")


def merge_sort(arr):
    global cnt
    cnt +=1
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left =  merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i=j=0
    while i< len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

while True:
    try:
        A, K = map(int, input().split())
        arr = list(map(int, input().split()))
        cnt = 0
        d = merge_sort(arr)

        if cnt<K:
            print(-1)
        else:
            print(d[K-1])
    except:
        break
