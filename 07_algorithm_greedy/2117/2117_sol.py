import sys
sys.stdin = open("2117_input.txt")

def (x,y,k, arr):
    # 중앙의 위치가 x,y임.
    global cnt
    if 0<=arr[x-k+1][y]<N


# 운영 비용 = K *K + (K-1)*(K-1)
# 도시를 벗어난 영역에 서비스를 제공해도 운영 비용은 변경되지 않는다
# 보안회사에서는 손해를 보지 않는 한 최대한 많은 집에 홈 방범 서비스를 제공하려고 한다
# 손해 보지 않으면서 홈방범 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾는다


T = int(input())
N, M = map(int, input().split())

# 집의 위치 확인하는 문제
arr = []
for i in range(N):
    line = list(map(int,input().split()))
    arr.append(line)

cnt =  0

