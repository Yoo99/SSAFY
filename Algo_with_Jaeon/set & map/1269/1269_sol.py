import sys
sys.stdin = open("1269_input.txt")

while True:
    try:
        A, B = map(int, input().split())
        list1 = set(map(int, input().split()))
        list2 = set(map(int, input().split()))
        s1 = len(list1-list2)
        s2 = len(list2- list1)
        print(s1+s2)
    except:
        break