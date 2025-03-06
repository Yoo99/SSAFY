# in 연산자
text = "hello world"
pattern = "world"

if pattern in text:
    print("패턴이 포함되어 있습니다.")

# find 메서드
text = "hello world"
pattern = "world"

pos = text.find(pattern)
# 찾는 패턴이 없으면 -1 반환
if pos != -1:
    print(f"패턴이 {pos}번째 위치에서 발견됨.")

# index 메서드드
# 는 패턴이 없으면 ValueError 발생
pos = text.index(pattern)

# 접두사/접미사
text = "hello world"
print(text.startswith("hello"))  # True
print(text.endswith("world"))    # True

# 패턴 등장 횟수
text = "hello hello world"
print(text.count("hello"))  # 2

# 패턴을 기준으로 나누어 리스트를 반환
text = "apple,banana,grape"
print(text.split(","))  # ['apple', 'banana', 'grape']

# 첫 번째 패턴을 기준으로, 앞 패턴 뒤  로 나누어 반환
text = "hello world"
print(text.partition(" "))  # ('hello', ' ', 'world')

# 특정 문자 제거
text = "  hello world  "
print(text.strip())  # "hello world"
text = "---hello---"
print(text.strip("-"))  # "hello"

# 특정 문자 필터링
words = ["apple", "banana", "apricot", "cherry"]
filtered = [word for word in words if word.startswith("a")]
print(filtered)  # ['apple', 'apricot']

# 패턴 삽입
words = ["apple", "banana", "cherry"]
print(", ".join(words))  # "apple, banana, cherry"
