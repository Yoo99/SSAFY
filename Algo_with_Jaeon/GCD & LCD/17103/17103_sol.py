import sys
sys.stdin = open("17103_input.txt")
import math

def div(n):
    if n==1:
        return None
    for i in range(2, int(math.sqrt(n))+1):
        if n%i ==0:
            return None
    return n


T = int(input()) # test case 의 개수
for _ in range(1, T+1):
    num = int(input())
    div_list = []
    for i in range(2,num//2+1):
        d = div(i)
        if d:
            e = num-d
            if div(e) == e:
                div_list.append((d,e))
    print(len(div_list))
