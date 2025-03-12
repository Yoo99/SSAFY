import sys
sys.stdin = open("5676_input.txt")

T = int(input())
for test_case in range(1, T+1):
    x1,y1,x2,y2 = map(int, input().split())
    lx1, ly1, lx2, ly2 = map(int, input().split())
    box_list= []
    for i in range(x1, x2+1): # y고정
        box_list.append((i,y1))
        box_list.append((i,y2))
    for j in range(y1, y2+1): # x 고정
        box_list.append((x1, j))
        box_list.append((x2,j))
    box_list = set(box_list)
    # 기울기 구하기
    # print(box_list)
    balance = (ly1-ly2)/(lx1-lx2)
    # b에 해당하는 값 구하기
    if ly1!=0 and lx1!=0:
        sub = ly1 - balance*lx1
    else:
        sub = ly2 - balance * lx2
    cnt = 0
    # 선분 안에 들어있는 점들 확인
    line_spot = []
    for lx in range(lx1, lx2):
        y = balance*lx + sub
        line_spot.append((lx,int(y)))
    for ele in line_spot:
        if ele in box_list:
            cnt +=1
        if cnt >3:
            break
    if cnt>3:
        print(f"#{test_case} 4")
    else:
        print(f"#{test_case} {cnt}")