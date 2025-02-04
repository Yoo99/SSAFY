import sys
sys.stdin = open("1231_input.txt", "r")


def inorder(idx):
    if idx >= len(data):
        return
    left = idx * 2
    right = idx * 2 + 1
    inorder(left)
    print(data[idx], end="")
    inorder(right)

for test_case in range(1,11):
    N = int(input())
    data = [None for _ in range(N+1)]

    for  i in range(N):
        line= list(input().split())
        data[int(line[0])] = line[1]

    # def get_left_child(data, index):
    #     left_index = index *2
    #     if left_index<len(data):
    #         return data[left_index]
    # def get_right_child(data, index):
    #     right_index = index*2 +1
    #     if right_index<len(data):
    #         return data[right_index]

    print(f"#{test_case} ",end ='')
    inorder(1)
    print()