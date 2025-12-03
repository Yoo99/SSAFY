import sys
from itertools import permutations
import heapq
sys.stdin = open("input.txt")

N = int(input()) # 숫자의 개수
num = list(map(int, input().split()))
sub = list(map(int, input().split()))
calc = ["+", "-", "*","/"]
calc_final = []
hq = []
for idx in range(len(sub)):
    sub_list = sub[idx] * calc[idx]
    calc_final += sub_list
for ele in permutations(calc_final):
    first =num[0]
    for id in range(0, len(num)-1):
        last = num[id+1]
        cal  = ele[id]
        if cal=='*':
            first *= last
        elif cal == "+":
            first += last
        elif cal == "/":
            if first <0:
                first *= (-1)
                first //=last
                first *=(-1)
            else:
                first //=last
        elif cal=="-":
            first -= last
    heapq.heappush(hq, first)
print(max(hq))
print(min(hq))