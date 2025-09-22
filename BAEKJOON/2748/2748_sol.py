import sys
sys.stdin = open("input.txt")

n = int(input())
fibo = [0, 1]
for idx in range(2, n+1):
    new_int = fibo[idx-1] + fibo[idx-2]
    fibo.append(new_int)
print(fibo[n])