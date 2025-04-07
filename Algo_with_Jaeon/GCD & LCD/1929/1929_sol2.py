import sys
sys.stdin = open("1929_input.txt")
import math

def div(n):
    if n ==1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
while True:
    try:
        n, m = map(int, input().split())
        for i in range(n, m+1):
            flag = div(i)
            if flag:
                print(i)
            else:
                continue
    except:
        break