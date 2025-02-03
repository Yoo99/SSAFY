import sys

sys.stdin = open('input.txt', 'r')
tc = int(input())
data = [list(map(int, input().split())) for _ in range(100)]
visit = [[0]*100 for _ in range(100)]

ans = []
for row in range(100):
    for col in range(100):
        if data[row][col] ==2:
            ans.append(row)
            ans.append(col)
print(ans)
row = ans[0]; col = ans[1]
print(row,col)
start_row, start_col = 0,0
if data[row][col-1] == 1:
    start_row = row; start_col = col-1
else:
    start_row = row-1 ; start_col = col
loc_list = []
for row in range(start_row,-1, -1):
    for col in range(start_col,-1,1):
        for dx, dy in [[-1,0],[0,-1]]:
            nx, ny = row+dx, col + dy
            print(nx)
            if 0<=nx<100 and 0<=ny<100 and visit[nx][ny] == 0 and data[nx][ny]==1:
                visit[nx][ny] = 1
                loc_list.append((nx,ny))

print(loc_list)

# 위 설정 이후부터는 매 input함수 호출시, 자동으로
# input.txt의 위에서부터 한줄 씩 읽어서 입력.
# for _ in range(10):
#     tc = int(input())
#     # 100 * 100 크기의 사다리 정보
#     # "0 1 0 1 0 1" -> 인덱스가 공백에도 주어져서 영 불편
#     '''
#     data = []
#     for i in range(100):
#         line = input()
#         # str.split(target)
#         # split 메서드는 문자열에서 target을 기준으로 쪼개서 새로운 리스트 반환
#         # 정수로 비교하는게 편함 -> 0은 False, 1은 True로 쓸 수 있거든
#         temp = []
#         for item in line.split():
#             temp.append(int(item))
#         data.append(temp)
#     print(data)
#     '''
#     # 입력받은 한줄을 공백 기준으로 쪼개서 리스트로 만든 다음
#     # map을 써서 각 요소를 int로 정수로 형 변환 한 다음
#     # 그 결과를 리스트로 변환
#     # 100번 반복
#     data = [list(map(int, input().split())) for _ in range(100)]
#     print(data)
#     result = 0
#     print(f"{tc} {result}")
