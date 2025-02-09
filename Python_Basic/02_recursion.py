def fact(n):
    if n ==0:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))

def fibonacci(n):
    if n ==1:
        return 1
    else:
        return n + fibonacci(n-1)
print(fibonacci(5))

numbers = [1,2,3]
result = map(str, numbers)
print(result)
print(list(result))
# zip 함수
girls = ['jane', 'ashley']
boys = ['peter','jay']
pair = zip(girls, boys)
print(pair)
print(list(pair))