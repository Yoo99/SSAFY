import sys
sys.stdin = open("23052_input.txt")

def combi(n, k):
    result = 1
    for i in range(k):
        result =result * (n-i)
    div = 1
    for j in range(k, 1, -1):
        div = div * j
    return result // div


T = int(input())
for test_case in range(1, T+1):
    n,a,b = map(int, input().split())
    print(f"#{test_case} {combi(n,a)}")