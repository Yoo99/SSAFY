def rabin_karp_rolling_hash(text, pattern):
    n = len(text)
    m = len(pattern)
    prime = 101 
    base = 256

    def calculate_hash(str):
        hash_value = 0
        for i, char in enumerate(str):
            # prime _ 모듈로 정의
            hash_value += ord(char) * pow(base, m-1-i, prime)
        return hash_value % prime # 나머지 값들만 가지고 반환해줄 것임

    pattern_hash = calculate_hash(pattern)
    window_hash = calculate_hash(text[:m])
    print(pattern_hash, "pattern")
    print(window_hash, "text[:m]")
    # 롤링 해시를 진행할 때, 최고 자리수 만큼 빼주기 위해 미리 연산

    highest_power = pow(base, m-1, prime)

    # text의 길이만큼 순회하면서 조사
    # pattern의 길이만큼은 제외하고 조사
    for i in range(n - m + 1):
        if window_hash == pattern_hash:
            # 두 개의 해시값이 일치하는 경우
            # 해시 함수를 통해서 만들어진 값이 ....
            # 서로 다른 문자열에 대해서도 동일한 해시값을 만들어 줄 수도 있다.
            # 이러한 경우를 해시 충돌이라고 한다.
            # 두 문자열 역시 일치하는지 확인하는 절차가 필요하다
            if text[i:i+m] == pattern:
                print(f"패턴: {i} - {i + m - 1}")

        # 해시값이 일치하지 않는 경우
        # 다음 윈도우로 이동하도록
        if i < n - m:
            # 첫 윈도우 문자에 해당하는 자릿수 값을 제거
            window_hash = window_hash - (ord(text[i]) * highest_power) % prime
            # 남은 해시값으로 한 자릿수 왼쪽으로 시프트
            window_hash = (window_hash * base) % prime
            # 다음 자리수 값을 해시값 처리한 다음
            window_hash = (window_hash + ord(text[i + m])) % prime

# 테스트
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print(f"텍스트: {text}")
print(f"패턴: {pattern}")
rabin_karp_rolling_hash(text, pattern)
