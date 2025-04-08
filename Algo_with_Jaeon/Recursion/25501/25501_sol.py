import sys
sys.stdin = open("25501_input.txt")

def recursion(s,l,r):
    global cnt
    cnt +=1
    if l>=r:
        return 1 , cnt
    elif s[l]!=s[r]:
        return 0 , cnt
    else:
        return recursion(s,l+1, r-1)


N = int(input()) # test_case의 숫자
for _ in range(N):
    cnt = 0
    s = input()
    d =  recursion(s, 0, len(s)-1)
    print(*d)