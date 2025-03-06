import sys
sys.stdin = open("14510_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
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

