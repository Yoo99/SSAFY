import math

def find(n):
    is_prime = [True] * (n+1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2,int(math.sqrt(n))+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime

n = 30
prim_flags = find(n)
for i in range(n+1):
    if prim_flags[i]:
        print(i, end = ' ')