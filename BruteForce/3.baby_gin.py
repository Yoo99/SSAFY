# baby-gin 검사
'''
- 숫자 3개가 연속되었는가 (run)
- 숫자 3개가 같은가 (triplet)
'''
# 6자리 숫자를 입력받는다
# -> 모든 순서를 보아야 한다. (순열)
#
used = [0] * 6
path = []
baby_gin_result = False

def is_baby_gin():
    cnt = 0
    # run + triplet 개수의 합 = 2

    # 앞쪽 숫자 3개 체크
    a, b, c = path[0], path[1], path[2]
    if a==b==c:# triplet
        cnt += 1
    elif a==(b-1)==(c-2):
        cnt+=1

    # 뒤 쪽 숫자 3개 체크
    a, b, c = path[3], path[4], path[5]
    if a == b == c:  # triplet
        cnt += 1
    elif a == (b - 1) == (c - 2):
        cnt += 1

    return cnt == 2

def recur(cnt):
    if cnt == 6:
        print(*path)
        if is_baby_gin():
            baby_gin_result = True
        return

    for idx in range(6):
        # idx 를 이미 썼다면, 뽑지 마라
        if used[idx]:
            continue
        used[idx] = 1
        path.append(arr[idx])
        recur(cnt+1)
        path.pop()
        used[idx] = 0


arr = [6,6,7,7,6,6]

recur(0)

print('YES') if baby_gin_result else print('NO')