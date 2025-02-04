import sys
sys.stdin = open("5432_input.txt", "r")

tc = int(input())
for test_case in range(1, tc+1):
    line = list(input())
    new_line = []
    count_box = 0;
    sum_count = count_box;
    for i in range(len(line)):
        if line[i] == "(":
            new_line.append("(")
        else:
            new_line.pop()
            if line[i-1]==")":
                sum_count +=1
            else:
                sum_count += len(new_line)
    print(f"{test_case} {sum_count}")