import sys
sys.stdin = open("1231_input.txt", "r")

for test_case in range(1,11):
    N = int(input())
    tree = [None for _ in range(N+1)]
    for row in range(N):
        line= list(input().split())
        idx= int(line[0])
        tree[idx] = line[1]
    ans = []
    def in_order(idx):
        if idx>=len(tree) or tree[idx] == None:
            return
        in_order(idx*2)
        ans.append(tree[idx])
        in_order(idx*2+1)
    in_order(1)
    answer = ''.join(ans)
    print(f"#{test_case} {answer}")