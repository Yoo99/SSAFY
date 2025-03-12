import sys
sys.stdin = open("5676_input.txt")

T = int(input())

for test_case in range(1, T+1):
    x1,y1, x2,y2 = map(int, input().split())
    lx1,ly1, lx2, ly2 = map(int, input().split())
    # 4개의 교차점
    spot = [(x1,y1),(x2,y2),(x1,y2),(x2,y1)]
    # 기울기가 0인경우
    cnt = 0
    if x1>x2:
        big_x ,small_x = x1, x2
    else:
        big_x,small_x = x2,x1
    if y1>y2:
        big_y, small_y= y1, y2
    else:
        big_y, small_y = y2, y1
    if (lx1==lx2) or (ly1==ly2):
        # 수직선일 때
        if lx1==lx2:
            if lx1 == x1 or lx1==x2:
                cnt =4
                print(f"#{test_case} {cnt}")
                continue
            elif lx1>small_x and lx1<big_x:
                cnt = 2
                print(f"#{test_case} {cnt}")
                continue
            else:
                cnt = 0
                print(f"#{test_case} {cnt}")
                continue
        # 수평선일 때
        elif ly1==ly2:
            if ly1 ==y1 or ly1 == y2:
                cnt =4
                print(f"#{test_case} {cnt}")
                continue
            elif ly1>small_y and ly1<big_y:
                cnt =2
                print(f"#{test_case} {cnt}")
                continue
            else:
                cnt = 0
                print(f"#{test_case} {cnt}")
                continue
    # 기울기가 0이 아닌 경우
    #
    else:
        # 꼭짓점과 만나는 갯수를 가지고 확인하기
        # 접선의 기울기
        line_balance = (ly1-ly2)/(lx1-lx2)
        # 상자의 중앙선
        box_balance = (y1-y2)/(x1-x2)
        if ly1 != 0 and lx1 != 0:
            sub = ly1 - balance * lx1
        else:
            sub = ly2 - balance * lx2
