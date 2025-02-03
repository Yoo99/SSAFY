import sys

sys.stdin = open('input.txt', 'r')
tc = int(input())

# 100x100 격자 데이터 입력
data = [list(map(int, input().split())) for _ in range(100)]
visit = [[0] * 100 for _ in range(100)]

# 2의 위치 찾기
ans = []
for row in range(100):
    for col in range(100):
        if data[row][col] == 2:
            ans.append((row, col))  # (row, col) 형태로 저장

print("2의 위치:", ans)  # 2의 위치 확인

# 2의 첫 번째 위치 선택
row, col = ans[0]  # (row, col) 형태이므로 그대로 할당
print("출발 좌표 (2 위치):", row, col)

# 시작 위치 찾기 (왼쪽 우선)
if col > 0 and data[row][col - 1] == 1:
    start_row, start_col = row, col - 1  # 왼쪽으로 이동
else:
    start_row, start_col = row - 1, col  # 위쪽으로 이동

print("탐색 시작 좌표:", start_row, start_col)

# 백트래킹 시작 (위쪽 이동 후 왼쪽 탐색)
loc_list = []

# 위쪽으로 먼저 이동
while start_row >= 0 and data[start_row][start_col] == 1:
    visit[start_row][start_col] = 1  # 방문 체크
    loc_list.append((start_row, start_col))
    start_row -= 1  # 위쪽으로 이동

# 왼쪽 이동 (start_row에서 왼쪽으로 이동 가능하면 계속 이동)
while start_col >= 0 and data[start_row + 1][start_col] == 1:
    visit[start_row + 1][start_col] = 1
    loc_list.append((start_row + 1, start_col))
    start_col -= 1  # 왼쪽으로 이동

# 디버깅용 출력 (어떤 좌표를 방문했는지)
print("방문한 좌표:", loc_list)