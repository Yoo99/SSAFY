import sys
sys.stdin = open("1225_input.txt", "r")


for test_case in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    while arr:
        d = arr.pop(0)
        count = count +1
        if count>5:
            count = count%5
        d -= count
        if d>0:
            arr.append(d)
        else:
            arr.append(0)
            break
    ans = ''
    for b in arr:
        ans+=str(b)+ " "
    print(f"#{test_case} {ans}")