import sys
sys.stdin = open("14510_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    M = max(data)
    diffs = [M- h for h in data]

    if sum(diffs)==0:
        print(f'#{test_case} 0')
        continue
    odd = sum(1 for d in diffs if d%2 ==1)
    x = odd # 홀수 개수

    while True:
        ones = (x+1)//2
        twos = x//2
        if ones < odd:
            x +=1
            continue
        even = sum(d//2 for d in diffs)
        if twos + (ones - odd) //2 >= even:
            print(f"#{test_case} {x}")
            break
        x += 1
