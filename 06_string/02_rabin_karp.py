def rabin_karp_rolling_hash(text, pattern):
    n = len(text)
    m = len(pattern)
    prime = 101 
    base = 256

    def calculate_hash(str):
        hash_value = 0
        for i, char in enumerate(str):
            hash_value += ord(char) * pow(base, m-1-i, prime)
        return hash_value % prime

    pattern_hash = calculate_hash(pattern)
    window_hash = calculate_hash(text[:m])
    highest_power = pow(base, m-1, prime)


    for i in range(n - m + 1):
        if window_hash == pattern_hash:
            if text[i:i+m] == pattern:
                print(f"패턴: {i} - {i + m - 1}")

        if i < n - m:
            window_hash = window_hash - (ord(text[i]) * highest_power) % prime
            window_hash = (window_hash * base) % prime
            window_hash = (window_hash + ord(text[i + m])) % prime

# 테스트
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print(f"텍스트: {text}")
print(f"패턴: {pattern}")
rabin_karp_rolling_hash(text, pattern)
