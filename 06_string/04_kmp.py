def get_lps(pattern):
    lps = [0] * len(pattern)
    j = 0
    i = 1

    while i < len(pattern):
        if pattern[j] == pattern[i]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j == 0:
                lps[i] = 0
                i += 1
            else:
                j = lps[j - 1]
    return lps


def kmp(text, pattern):
    M = len(pattern)
    N = len(text)
    lps = get_lps(pattern)

    i = 0
    j = 0

    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == M:
            print(f"패턴 {i - j}에서 발견")
            j = lps[j - 1]

        elif i < N and pattern[j] != text[i]:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]


text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp(text, pattern)
