import sys
sys.stdin = open("input.txt")

N = int(input())
v = [0] * (N+1)

for i in range(2, N+1):
    v[i] = v[i-1] +1
    if i%2==0:
        v[i] = min(v[i], v[i//2] +1)
    if i%3 == 0:
        v[i] = min(v[i], v[i//3]+1)
print(v[N])