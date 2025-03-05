# 오름차순 정렬
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)  # [1, 2, 5, 5, 6, 9]

# 내림차순 정렬
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 5, 2, 1]

# 문자열 정렬
words = ["banana", "apple", "Cherry", "kiwi"]
words.sort() # 대문자로 되어 있는 애부터 정렬된다
print(words)    # 출력: ['Cherry', 'apple', 'banana', 'kiwi']

# 문자열 길이순 정렬
words = ["banana", "apple", "cherry", "kiwi"]
words.sort(key=len) # key를 설정함으로써 정렬의 기준을 무엇으로 할 것인가를 정해
print(words)    # ['kiwi', 'apple', 'banana', 'cherry']

# 튜플 정렬
pairs = [(3, "three"), (1, "one"), (4, "four"), (2, "two")]
pairs.sort()
print(pairs)    # [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

# 튜플 두번째 요소를 기준으로 정렬
pairs = [(3, "three"), (1, "one"), (4, "four"), (2, "two")]
pairs.sort(key=lambda x: x[1])
print(pairs)    # [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# 딕셔너리 정렬
students = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 22},
    {"name": "Bob", "age": 24}
]
# 나이를 기준으로 정렬
students.sort(key=lambda x: x["age"])
print(students)
# 출력: [{'name': 'Alice', 'age': 22}, {'name': 'Bob', 'age': 24}, {'name': 'John', 'age': 25}]

# 여러 기준으로 정렬
students = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 22},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 25}
]
students.sort(key=lambda x: (x["age"], x["name"]))
print(students)
# 출력: [{'name': 'Alice', 'age': 22}, {'name': 'Bob', 'age': 22}, {'name': 'Charlie', 'age': 25}, {'name': 'John', 'age': 25}]