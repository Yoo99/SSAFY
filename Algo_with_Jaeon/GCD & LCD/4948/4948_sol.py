import sys
sys.stdin = open("4948_input.txt")
import math

def div(n):
    if n ==1:
        return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1


while True:
    try:
        n = int(input())
        if n ==0:
            break
        cnt = 0
        for j in range(n+1 ,2*n+1):
            cnt += div(j)
        print(cnt)
    except:
        break