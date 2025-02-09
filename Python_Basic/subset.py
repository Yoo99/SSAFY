# arr = [2,3,7]
# bit  = [0] * 3
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             s = 0 # 부분 집합의 합
#             for b in range(3):
#                 if bit[b]:
#                     print(arr[b], end = ' ') # ㅂ분집합에 포함된 원소
#                     s += arr[b]
#             print(bit ,s)

arr = [3,6,7,1,5,4]
n = len(arr)
for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end = ", ")
    print()
print()
