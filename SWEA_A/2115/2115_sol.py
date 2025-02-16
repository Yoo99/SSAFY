import sys
sys.stdin = open("2115_input.txt","r")

T = int(input())
for test_case in range(1, T+1):
    N,M,C = map(int, input().split())
    arr=[]
    for row in range(N):
        line = list(map(int, input().split()))
        arr.append(line)
    # print(arr)
    visited = [[False]* N for _ in range(N)]
    selected = []
# sub
#                       -3     -2     -1
# sub [num, num.... , row, col, profit]
    for row in range(N):
        for col in range(N-M+1):
            sub = arr[row][col:col+M]
            profit = 0
            if sum(sub)>C:
                while sum(sub)>C:
                    d = min(sub[0], sub[-1])
                    # print(d)
                    sub.remove(d)
            sub.append(row)
            sub.append(col)
            for b in range(0, len(sub)-2):
                d = sub[b]*sub[b]
                profit +=d
            sub.append(profit)
            selected.append(sub)
    # print(selected)
    sort_selected = sorted(selected, key = lambda x:x[-1], reverse = True)
    # print(sort_selected)
    ans = []
    d = sort_selected.pop(0)
    ans.append(d)
    row, col = ans[0][-3:-1]

    for ele in sort_selected:
        # if ele[-3] == row and not (ele[-2]+M <=ans[0][-2] or ans[0][-2]+M<=ele[-2]):
        if ele[-3] != row or (ele[-2] + M <= ans[0][-2] or ans[0][-2] + M <= ele[-2]):
            ans.append(ele)
            break
        else:
            continue
    total_profit = 0
    for b in ans:
        total_profit += b[-1]
    print(f"#{test_case} {total_profit}")