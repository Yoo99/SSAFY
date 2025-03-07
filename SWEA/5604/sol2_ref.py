import sys
sys.stdin = open("5604_input.txt")

def digit_sum(n):
    total = 0
    for num in range(1, n+1):
        total += sum(int(digit) for digit in str(num))
    return total

def range_digit_sum(start, end):
    return digit_sum(end) - digit_sum(start-1)

T = int(input())
for test_case in range(1, T+1):
    start,end = map(int, input().split())
    print(f"#{test_case} {range_digit_sum(start,end)}")
