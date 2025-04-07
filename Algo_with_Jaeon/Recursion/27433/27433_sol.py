import sys
sys.stdin = open("27433_input.txt")

def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)

while True:
    try:
        n = int(input())
        print(fact(n))
    except:
        break