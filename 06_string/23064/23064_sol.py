import sys
sys.stdin = open("23064_input.txt")

T = int(input())
for test_case in range(1, T+1):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))
    k = len(str1)
    result = 0
    for i in range(0, len(str2)-k+1):
        sub_str = str2[i:i+k]
        if (''.join(sub_str)) == (''.join(str1)):
            result =1
            break
    print(f"#{test_case} {result}")