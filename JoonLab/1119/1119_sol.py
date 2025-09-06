import sys
sys.stdin = open("input.txt")

n = int(input())

def fibonacci(n):
    if n<=2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(n))