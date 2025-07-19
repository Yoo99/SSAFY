import sys
sys.stdin = open("1486_input.txt")

def find_height(idx, cur_height):
    global min_height
    global B
    # print(idx, cur_height)
    if cur_height>=B:
        min_height = min(min_height, cur_height)
        return
    if idx == len(height):
        return
    find_height(idx+1,cur_height+height[idx])
    find_height(idx+1, cur_height)

T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    min_height = 100000000
    find_height(0,0)
    print(f"#{test_case} {min_height-B}")