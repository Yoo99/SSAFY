def build_bad_char_heuristic(pattern):
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i
    return bad_char

def boyer_moore(text, pattern):
    bad_char = build_bad_char_heuristic(pattern)
    print(bad_char)
    m = len(pattern)
    n = len(text)
    i = 0

    while i <= n - m:
        j = m - 1 # 비교해야 하는 값만 잘 처리해주면 된다

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            print(f"패턴이 위치 {i}에서 발견되었습니다.")
            i += 1

        else:
            skip = j - bad_char.get(text[i + j], -1)
            i += max(1, skip)

text = "ABAAABCDAAABCABAAABCABAB"
pattern = "AAABCABAB"
print(f"텍스트: {text}")
print(f"패턴: {pattern}")
boyer_moore(text, pattern)