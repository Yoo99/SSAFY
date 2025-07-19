'''
부분 집합의 개수 => (1<<len(arr))
'''
arr = ['A','B','C']
n = len(arr) # arr의 길이

def get_sub(tar):
    print(f'target = {tar}', end = '/')
    for i in range(n):
        #각각 원소가 포함되어 있나요?
        if (tar>>i) & 0x1: # 각 자리의 원소가 포함되어 있나요?
            print(arr[i], end = '')
            '''
            맨 우측 비트를 삭제한다 
            다음 원소를 확인하겠다 
            '''
# 전체 부분집합을 확인해야 한다
for target in range(1<<n):
    get_sub(target)
    print()