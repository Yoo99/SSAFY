kr_scores = [10,20,30,40,50]
math_scores = [20, 40, 50, 70,80]
en_scores = [40, 20, 30, 50 ]

for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)

def func():
    num = 20
    def rep():

        print('local', num)

# rep()
# print('global', num)

cnt = 0
def increment():
    print(cnt)
    global cnt
    cnt +=1
print(cnt)
increment()
print(cnt)
# 함수 하나가 여러 가지의 책임을 가지게 만들지 말 것
