def binarySearch(a, N, key):
    start = 0
    end = N-1
    while start<=end:
        middle=  (start+end) //2
        if a[middle] == key:
            return middle
        elif a[middle] > key :
            end = middle-1
        else:
            start = middle+1
    return -1

arr = [2, 4, 7, 9, 11, 19, 23]
