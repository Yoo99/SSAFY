import sys
sys.stdin = open("23053_input.txt")

# A씨는 박스에 담긴 물건의 가격 합계가 최대가 되도록 물건을 담으려고 한다
# A씨 차례에 남은 물건의 크기와 가격이 주어질 때, A씨가 담을 수 있는 물건 가격은
# 최대 얼마인지 알아내는 프로그램을 작성하시오
# 담긴 상품의 크기 합이 박스 크기를 초과할 수 없다

def generate_subsets(arr):
    n = len(arr)
    subsets = []
    for bitmask in range(1<<n):
        subset = []
        for i in range(n):
            if bitmask & (1<<i):
                subset.append(arr[i])
        subsets.append(subset)
    return subsets

T = int(input())
for test_case in range(1, T+1):
    box_list = []
    N, M = map(int, input().split())
    for _ in range(M):
        s, p = map(int, input().split())
        box_list.append((s,p))
    box_list.sort()
    subsets = generate_subsets(box_list)
    max_val = 0
    for ele in subsets:
        box_size = 0; val = 0
        for b in ele:
            box_size += b[0]
            val += b[1]
        if box_size<=N:
            if val>max_val:
                max_val = val
    print(f"#{test_case} {max_val}")
