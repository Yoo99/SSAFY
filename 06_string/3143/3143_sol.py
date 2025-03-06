import sys
sys.stdin = open("3143_input.txt")

T= int(input())
for test_case in range(1, T+1):
    str1, str2 = map(str, input().split())
    # str2의 문자열 길이
    k = len(str2)
    count = 0
    i=0
    while i <= len(str1)-k:
        if str1[i:i+k] == str2:
            count +=1
            i = i+k
        else:
            i +=1
    rest = len(str1) - count*k
    count += rest

    print(f"#{test_case} {count}")
