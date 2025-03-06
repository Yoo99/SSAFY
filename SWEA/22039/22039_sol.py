import sys
sys.stdin = open("22039_input.txt")

def fibonacci(n):
    fibo = [0]*(n+1)
    fibo[1] = 1
    if n>1:
        fibo[2] = 1
    for i in range(3, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo

def partition_fibonacci(n):
    fibo  = fibonacci(n)
    total_sum = sum(fibo)
    if total_sum%2 !=0:
        return "impossible"

    mid = total_sum//2
    subset = set()
    current_sum = 0
    for i in range(n, 0, -1):
        if current_sum + fibo[i] <= mid:
            current_sum += fibo[i]
            subset.add(i)
    if current_sum != mid:
        return "impossible"
    else:
        result = ["B"] * (n)
        for i in subset:
            result[i-1] = "A"
        return result
T = int(input())
for test_case in range(1, T+1):
    N  = int(input())
    print(f"{''.join(partition_fibonacci(N))}")