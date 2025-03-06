def bruteforce(p, t):
    M = len(p)
    N = len(t)

    i = j = 0

    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1

        i += 1
        j += 1

    if j == M:
        return i - M
    else:
        return i

str = "123456789"
ch = "34"

result = bruteforce(str,ch)
print(result)
