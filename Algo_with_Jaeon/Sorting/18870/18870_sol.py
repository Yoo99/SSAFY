import sys
sys.stdin = open("18870_input.txt")

while True:
    try:
        _ = int(input()) # N개의 숫자 리스트
        length = list(map(int ,input().split()))
        min_num = min(length)
        set_sublst = sorted(set(length))
        num_to_index = {num:idx for idx, num in enumerate(set_sublst)}
        for num in length:
            print(num_to_index[num], end = ' ')
        print()
    except:
        break