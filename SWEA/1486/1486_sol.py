import sys
sys.stdin = open("1486_input.txt")

def recur(idx,cur_height):
    global min_height
    global height
    global B # 선반의 높이
    if cur_height>=B:
        return
    if idx == len(height):
        if
        min_height = min(min_height, cur_height)
        return
    recur(idx+1, cur_height + height[idx])
    # print(height[idx])
    recur(idx+1, cur_height)

T = int(input()) # test_case 개수
for test_case in range(1, T+1):
    N, B = map(int,input().split()) # 점원의 수, 탑의 높이
    height = list(map(int, input().split())) # 점원들의 키 리스트
    min_height = 10000000
    recur(0,0)
    print(min_height)
