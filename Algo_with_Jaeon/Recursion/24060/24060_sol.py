import sys
sys.stdin = open("24060_input.txt")


def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left =  merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    i, j=  0, 0
    while i<=len(left) and j<=len(right):
        if



while True:
    try:
        A, K = map(int, input().split())
        arr = list(map(int, input().split()))
        cnt = 0
