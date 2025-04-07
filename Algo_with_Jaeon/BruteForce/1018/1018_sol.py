import sys
sys.stdin = open("1018_input.txt")

def compare1(chess):
    global cnt1
    for i in range(8):
        for j in range(8):
            if (i+j) %2 ==0 and chess[i][j] == 'W':
                continue
            elif (i+j)%2 ==1 and chess[i][j] =='B':
                continue
            else:
                cnt1 +=1

    return cnt1
def compare2(chess):
    global cnt2
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0 and chess[i][j] =='B':
                continue
            elif (i+j)%2 ==1 and chess[i][j] =='W':
                continue
            else:
                cnt2+=1
    return cnt2

while True:
    try:
        M, N = map(int, input().split()) # M :행의 개수, N: 열의 개수
        arr = [list(map(str, input())) for _ in range(M)]

        min_count = []
        for row in range(0, M-8+1): # 행의 길이를 제한하는 것
            for col in range(0, N-8+1):
                chess = []
                for idx in range(row, row +8):
                    line = arr[idx][col:col+8]
                    chess.append(line)
                cnt1 , cnt2 = 0,0
                d1 = compare1(chess)
                d2 = compare2(chess)
                min_count.append(min(d1, d2))
        print(min(min_count))
    except:
        break
