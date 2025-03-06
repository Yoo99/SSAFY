def bruteforce(target, pattern):
    target_len = len(target)
    pattern_len = len(pattern)
    target_idx = 0  # 전체 문자열 탐색 인덱스
    pattern_idx = 0  # 패턴 탐색 인덱스

    while target_idx < target_len:
        if target[target_idx] == pattern[pattern_idx]:  # 값이 일치하면
            pattern_idx += 1  # 패턴 인덱스 증가
            if pattern_idx == pattern_len:  # 패턴 전체를 찾은 경우
                return target_idx - pattern_len + 1  # 패턴의 시작 위치 반환
        else:
            target_idx -= pattern_idx  # 검사 시작 위치를 한 칸 뒤로 이동
            pattern_idx = 0  # 패턴 인덱스 초기화

        target_idx += 1

    return -1  # 패턴을 찾지 못한 경우

# 테스트
target_str = "123456789"
pattern_str = "34"

result = bruteforce(target_str, pattern_str)
print(result)  # 2 출력 (0-based index)
