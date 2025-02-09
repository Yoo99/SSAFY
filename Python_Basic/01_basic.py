def my_func():
    print("hello")
result = my_func()
print(result)
## 매개변수와 인자
"""
매개변수 : 함수를 정의할 때, 함수가 받을 값을 나타내는 변수
인자: 함수를 호출할 때, 실제로 전달되는 값 
"""
def greet(name, age):
    print(f"안녕하세요 {name}님! {age}살이시군요.")

greet("Alice", 25)
# greet(age=35, "DAVE") : positional error
greet("DAVE", age = 35 )

# 튜플은 의도하기보다는 내부 동작에서 활용된다.
def print_info(**kwargs):
    print(kwargs)
print_info(name = "EVE", age = 30)

def func(pos1, pos2, default_arg = "defaul", *args, **kwargs):
    print('pos1:',pos1)
    print('pos2:', pos2)
    print("default_arg", default_arg)
    print("args:", args)
    print("kwargs:", kwargs)
func(1,2,3,4,5,6, key1='value1', key2 = 'value2')