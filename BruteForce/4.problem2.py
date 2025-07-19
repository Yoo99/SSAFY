'''
baby-gin 검사
- 숫자 3개가 연속되었는가 (run)
- 숫자 3개가 같은가 (triplet)
6자리 숫자를 입력
-> 모든 순서를 보아야 한다(순열)
'''
used = [0] * 6
path = []

def is_baby_gin():
    cnt = 0
    # run + triplet 개수의 합 = 2
    a,b,c = path[0],path[1],path[2]
    if a==b==c: # triplet
        cnt +=1
    elif a ==(b-1)==(c-2):
        cnt +=1
    # 뒤쪽 숫자 3개에 대해서도 검사 진행하기
    a,b,c = path[3],path[4],path[5]
    if a==b==c: # triplet
        cnt +=1
    elif a==(b-1)==(c-2): # run
        cnt +=1

    return cnt ==2



def recur(cnt):
    global baby_gin_result
    if cnt == 6:
        # baby-gin 인지 검사
        if is_baby_gin():
            baby_gin_result = True
        return
    for idx in range(6):
        # idx를 이미 썼다면, 뽑지 마라
        if used[idx]:
            continue
        used[idx] =1
        path.append(arr[idx])
        recur(cnt+1)
        path.pop()
        used[idx] = 0
    return baby_gin_result

# arr = list(map(int, input().split()))
arr = [6,6,7,7,6,7]
baby_gin_result = False
print(recur(0))