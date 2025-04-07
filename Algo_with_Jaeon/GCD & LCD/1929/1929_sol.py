import sys
sys.stdin = open("1929_input.txt")

def div(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True
while True:
    try:
        n, m = map(int, input().split())
        for i in range(n, m+1):
            flag = div(i)
            if flag == True:
                print(i)
            else:
                continue
    except:
        break