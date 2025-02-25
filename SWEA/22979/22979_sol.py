import sys
sys.stdin = open("22979_input.txt")

T = int(input())
for test_case in range(1, T+1):
    arr = list(input())
    K = int(input())
    cal = list(map(int, input().split()))
    for ele in cal:
        if ele>0:
            e = arr[:ele]
            arr = arr[ele:] +e
        elif ele<0:
            for i in range(abs(ele)):
                d = arr[-1]
                arr = [d] + arr[:-1]
        elif ele ==0:
            continue
    print(''.join(arr))
    