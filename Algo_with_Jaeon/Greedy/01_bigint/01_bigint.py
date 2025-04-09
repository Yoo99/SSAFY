import sys
sys.stdin = open("input.txt")

def greedy(arr, M, K):
    arr.sort(reverse = True)
    sum = 0
    i = 0
    while M>0:
        if M == 0:
            break
        i =  i%2
        if i == 0:
            if M > K:
                sum += (arr[i] * K)
                M -= K
                i +=1
            else:
                sum += (arr[i] * M)
                M =0
                i+=1
        else:
            sum += arr[i]
            M -=1
            i +=1
    return sum


while True:
    try:
        N, M, K = map(int, input().split())
        arr = list(map(int, input().split()))
        print(greedy(arr, M, K))
    except:
        break