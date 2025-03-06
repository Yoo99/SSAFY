import sys
sys.stdin = open("14510_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))
    find_max = max(height)
    count_days = 0; round = 0
    height = [abs(i-find_max) for i in height]
    while sum(height)>0:
        if sum(height)==0:
            break
        round += 1
        height.sort(reverse = True)
        height = [i for i in height if i!=0]
        if round %2 ==1:
            height[-1] -=1
            count_days +=1
        elif round%2 ==0:
            if height[0]-2<0:
                continue
            else:
                height[0]-=2
            count_days+=1
    print(f"#{test_case} {count_days}")