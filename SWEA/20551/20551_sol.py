import sys
sys.stdin = open("20551_input.txt")

T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    arr.reverse()
    sum = 0
    ans  = -1
    flag = True
    while flag:
        d1 = arr.pop(0)
        for i in range(2):
            d2 = arr.pop(0)
            if d1>d2:
                sum +=0
            elif d1==d2:
                d2 -=1
                if d2>0:
                    sum +=1
                else:
                    sum = -1
                    flag = False
            else:
                d2 -=(d2-d1+1)
                if d2>0:
                    sum +=(d2-d1+1)
                else:
                    sum = -1
                    flag = False
            d1 = d2
        break

    print(f"#{test_case} {sum}")
