import sys
sys.stdin = open("5643_input.txt")
from collections import deque

T = int(input())
N = int(input()) # 학생들의 숫자
M = int(input()) # 학생들의 키를 비교한 결과
keys = [i for i in range(1, N+1)]
student = {key:[] for key in keys}

for j in range(M):
    a,b = map(int, input().split())
    student[a].append(b)
print(student)
height = deque()

for key,value in student:
    if value != []:
        if key not in height:
            height.appendleft(key)
            height.append()


