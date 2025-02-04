import sys
sys.stdin = open("1232_input.txt")
for test_case in range(1,11):
    N = int(input())
    line = [None for _ in range(N+1)]
    for i in range(N):
        li = input().split()
        line[int(li[0])] = li[1]
    # for b in line:
    #     print(b, type(b))
    ans = []

    def postorder(idx):
        if idx<len(line) and line[idx]:
            left = idx*2
            right = idx*2+1
            postorder(left)
            postorder(right)
            ans.append(line[idx])
    postorder(1)
    print(ans)
    sum = 0
    # while ans:
    #     d = ans.pop(0)
    #     if d not in ("*","+","-","/"):
    #         sum += int(d)
    #     else:
    #         d2 = int(ans.pop(0))
    #         if d =="*":
    #             sum *= d2
    #         elif d == "+":
    #             sum += d2
    #         elif d =="-":
    #             sum -= d2
    #         else:
    #             sum /=d2
    print(sum)
    print(f"#{test_case} {int(sum)}")
