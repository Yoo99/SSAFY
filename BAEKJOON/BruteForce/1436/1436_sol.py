import sys
sys.stdin = open("1436_input.txt")
while True:
    try:
        N = int(input())
        cnt = 0
        num = 666

        while True:
            str_num = str(num)
            if "666" in str_num:
                cnt +=1
            if N == cnt:
                break
            num +=1

        print(num)
    except:
        break