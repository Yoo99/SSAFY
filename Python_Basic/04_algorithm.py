# arr = [78,42,55,12,21]
# N = len(arr)
# for i in range(0, N-1):
#     for j in range(0, N-i-1):
#         if arr[j] >arr[j+1]:
#             arr[j+1],arr[j] =  arr[j], arr[j+1]
#         else:
#             continue
# print(arr)

# Counting 알고리즘
'''
DATA[i]는 0이상 4이하라는 조건이 있는 경우 
'''
DATA  = [0,4,1,3,1,2,4,1]
N = len(DATA)
COUNTS =  [0] * (max(DATA) +1) # max(DATA) +1

for i in range(N):
    COUNTS[DATA[i]] += 1

for i in range(1, len(COUNTS)):
    COUNTS[i] += COUNTS[i-1]

print(COUNTS)

TEMP = [0]* len(DATA)
print(TEMP)
for i in range(len(DATA)-1,-1,-1):
    print(DATA[i])
    COUNTS[DATA[i]] -= 1  # DATA[i]까지의 개수 1개를 감소
    TEMP[COUNTS[DATA[i]]] = DATA[i]

