import sys
sys.stdin = open("1232_input.txt")

cal = ["-","+","*","/"]
for test_case in range(1,11):
    N = int(input())
    tree = [None for _ in range(N+1)]
    default = []
    for i in range(N):
        line= list(input().split())
        default.append(line)
    for line in default:
        if line[1] not in cal:
            idx, val = int(line[0]), int(line[1])
        else:
            idx, val = int(line[0]), line[1]
        tree[idx] = val
    default.reverse()
    # print(default)
    for ele in default:
        if len(ele) ==2:
            continue
        else:
            idx = int(ele[0])
            if ele[1] == cal[0]:
                tree[idx] = tree[int(ele[2])] - tree[int(ele[3])]
            elif ele[1] == cal[1]:
                tree[idx] = tree[int(ele[2])] + tree[int(ele[3])]
            elif ele[1] == cal[2]:
                tree[idx] = tree[int(ele[2])] * tree[int(ele[3])]
            elif ele[1] ==cal[3]:
                tree[idx] = tree[int(ele[2])]//tree[int(ele[3])]
    print(f"#{test_case} {tree[1]}")