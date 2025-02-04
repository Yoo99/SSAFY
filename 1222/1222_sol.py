import sys
sys.stdin = open("1222_input.txt", "r")

for test_case in range(1, 11):
    n = int(input())
    arr = list(input())
    sum = 0
    for i in range(len(arr)):
        d = arr.pop()
        if d == "+":
            continue
        else:
            sum +=int(d)
    print(f"#{test_case} {sum}")