import sys
sys.stdin = open("input.txt")

num = list(map(int, input()))
num.reverse()
result = []
for ele in num:
    if not result and ele ==0:continue
    result.append(ele)
    print(ele, end= '')
print()