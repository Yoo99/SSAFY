import sys
sys.stdin = open('1208_input.txt')

for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    while cnt<N:
        if cnt ==N:
            break
        max_num = max(arr)
        min_num = min(arr)
        arr.append(max_num-1)
        arr.append(min_num+1)
        arr.remove(max_num)
        arr.remove(min_num)
        if (max(arr) - min(arr))==1 or (max(arr) - min(arr)==0):
            break
        cnt +=1
    print(max(arr)- min(arr))