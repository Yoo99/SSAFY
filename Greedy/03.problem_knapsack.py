n = 3
target = 30
things = [(5, 50),(10,60), (20, 140)]

# kg당 가격으로 어떻게 정렬?
# 정렬 : (price/kg)
# lambda: 재사용하지 않는 함수
'''
정리 
1. 부분집합 
    - 비트연산 
    - 재귀호출
2. 조합 
    - 재귀호출 (중복순열, 순열)
3. 그리디
    - 많이 풀어봐야 한다. 
    (규칙을 못찾으면 못푼다) 

'''
things.sort(key=lambda x:(x[1]/x[0]), reverse = True)
print(things)