import sys
sys.stdin = open("23067_input.txt")

def find_mid(cnt, start, end, val):
    cnt +=1
    mid= (start+end)//2
    # print(mid)
    if val == mid:
        return 1, cnt
    if val >mid:
        return find_mid(cnt,mid, end, val)
    elif val < mid:
        return find_mid(cnt,start, mid, val)
    return 0, cnt


T = int(input())

for test_case in range(1, T+1):
    P, A, B = map(int, input().split())
    start ,end = 1, P
    cnt_a , cnt_b = 0, 0
    ans_a, cnt_a = (find_mid(cnt_a,start,end, A))
    ans_b, cnt_b = (find_mid(cnt_b,start, end, B))
    if cnt_a<cnt_b:
        print(f"#{test_case} A")
    elif cnt_a > cnt_b:
        print(f"#{test_case} B")
    else:
        print(f"#{test_case} 0")
