# 0 ~ 9의 번호가 적혀있는 카드가 6장 존재한다
'''
3장의 카드가 연속적인 번호를 갖는 경우 'run'이라고 하고,
3장의 카드가 동일한 번호를 갖는 경우 'triplet'이라고 한다
그리고 6장의 카드가 run과 triplet으로만 구성된 경우를 baby-gin으로 부른다
'''

# def baby_gin(path):
#     if len(path) == 6:
#         # 이때, run과 triplet을 확인한다
#         path.sort() #정렬
#         # triplet인 경우:
#         for ele in path:
#             if path.count(ele) ==3:
#                 triplet +=1
#         return
#     for i in range(0, 9):
#         path.append(i)
#         baby_gin(path)
#         path.pop()

number = [0,1,7,2,7,7]
triplet, run = 0, 0


def baby_gin(number):
    global triplet, run
    number.sort()
    for ele in set(number):
        if number.count(ele) == 3:
            triplet +=1
            for _ in range(3):
                number.remove(ele)
    for i in range(0,len(number)-2):
        if number[i]+1 == number[i+1] and number[i+1]+1 ==number[i+2]:
            run +=1
            number = number[0:i] + number[i+3:]
    if (triplet ==1 and run ==1) or triplet ==2 or run==2:
        return True
    return False, triplet, run
print(baby_gin(number))
num2 = [3,3,3,1,2,3]
print(baby_gin(num2))

# answer
used = [0] * 6
path = []
baby_gin_result = False
def is_baby_gin():
    cnt = 0
    # run + triplet 개수의 합 = 2
    a,b,c = path[0], path[1], path[2]
    if a==b==c:
        cnt +=1
    elif a==(b-1) and b==(c-1):
        cnt +=1
    # 뒤쪽에 있는 숫자 3개도 검사해주어야 한다
    d,e,f = path[3],path[4],path[5]
    if d==e==f:
        cnt +=1
    elif d==(e-1) == (f-2):
        cnt +=1
    return cnt ==2

def recur(cnt):
    global baby_gin_result
    if cnt == 6:
        # baby-gin인지 검사
        if is_baby_gin():
            baby_gin_result = True
        return

    for idx in range(6):
        # idx 를 이미 썼다면 뽑지 말라
        if used[idx]:
            continue
        used[idx] = 1
        path.append(arr[idx])
        recur(cnt+1)
        path.pop()
        used[idx] = 0
arr = [6,6,7,7,6,7]
recur(0)