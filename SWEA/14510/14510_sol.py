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

    height= list(map(int, input().split()))
    max_height = max(height)
    height=  [max_height - i for i in height]

    if sum(height) ==0:
        print(f"#{test_case} 0")
        continue
    odd = sum(1 for x in height if x%2==1) # 최소로 홀수 날짜가 필요한 경우
    x = odd

    while True:
        ones = (x+1) // 2
        twos = x//2

        if ones < odd:
            x+=1
            continue
        even = sum(d//2 for d in height)

        if twos + (ones-odd)//2 >=even:
            print(f"#{test_case} {x}")
            break
        else:
            x+=1


