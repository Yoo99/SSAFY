import sys
sys.stdin = open("10870_input.txt")

def fibo(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

while True:
    try:
        n = int(input())
        print(fibo(n))
    except:
        break
