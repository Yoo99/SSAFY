import sys
sys.stdin = open("input.txt")

A = list(map(int, input().split()))
B = list(map(int, input().split()))
a,b = 0, 0
for idx in range(len(A)):
    if A[idx] > B[idx]:
        a+=1
    elif B[idx]>A[idx]:
        b+=1
    else:
        continue
if a>b:
    print(1)
else:
    print(0)