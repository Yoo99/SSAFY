import sys
sys.stdin = open("input.txt")

n = int(input()) # 질의 개수
visited = [0 for _ in range(23*60*60 + 59*60+59+1)]
for _ in range(n):
    type, start, end = input().split()
    if type == "1":
        hh, mm, ss = map(int, start.split(":"))
        start_x = hh * 60*60 + mm*60  + ss
        h2, m2, s2 = map(int, end.split(":"))
        end_x = h2 * 3600 + m2 * 60 + s2
        for i in range(start_x, end_x):
            visited[i] += 1
    elif type == "2":
        hh, mm, ss = map(int, start.split(":"))
        start_time = hh * 60 * 60 + mm * 60 + ss
        h2, m2, s2 = map(int, end.split(":"))
        end_time = h2 * 3600 + m2 * 60 + s2
total = 0
for b in range(start_time, end_time):
    total += visited[b]
print(total)
