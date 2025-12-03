'''
그리디로 풀 수 있는 조건
1. 탐욕적 선택 조건 ( greedy choice property)
- 각 단계의 최적해 선택이 이후 단계 선택에 영향을 주지 않는다
- 즉 각 단게의 규칙이 변하면 안된다.
2. 최적 부분 구조 (Optmal Substructure)
- 각 단계의 최적해 선택이 전체 문제의 해결책이어야 한다.
'''

coin_list = [500, 100, 50, 10]
target = 1730
cnt = 0
for coin in coin_list:
    possible_cnt = target //coin
    cnt += target//coin
    target = coin * possible_cnt

print(cnt)
