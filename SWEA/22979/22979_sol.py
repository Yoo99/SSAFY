import sys
sys.stdin = open("22979_input.txt")

T = int(input())
for test_case in range(1, T+1):
    arr = list(input())
    K = int(input())
    cal = list(map(int, input().split()))
    for ele in cal:
        if ele == 0:continue
        elif ele <0:
            if abs(ele)>len(arr):
                ele = abs(ele)%len(arr) * (-1)
            e = arr[ele:]
            arr = e + arr[:ele]
        else:
            if ele>len(arr):
                ele = ele%len(arr)
            e = arr[:ele]
<<<<<<< HEAD
            arr = arr[ele:] +e
        elif ele<0:
            for i in range(abs(ele)):
                d = arr[-1]
                arr = [d] + arr[:-1]
        elif ele ==0:
            continue
    print(''.join(arr))
    
=======
            arr = arr[ele:] + e

    print(''.join(arr))
>>>>>>> 0dd699f0e70f3a1a658e9fb2f51913ef87901dce
