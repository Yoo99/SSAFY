import sys
sys.stdin = open("4698_input.txt")

T = int(input())
for test_case in range(1, T+1):
    D, A, B = map(int, input().split())
    arr = [i for i in range(A, B+1) if str(D) in str(i)]
    # print(arr)
    arr_list = []
    for d in arr:
        if d==2:
             arr_list.append(d)
        elif d>2:
            is_prime = True
            for i in range(2, int(d**(0.5))+1,1):
                if d % i ==0:
                    is_prime = False
                    break
            if is_prime:
                arr_list.append(d)
    print(f"#{test_case} {len(arr_list)}")
