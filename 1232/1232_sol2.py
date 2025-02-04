import sys
sys.stdin = open("1232_input.txt", "r")

N = int(input())
dict = {}
print(N)
for  i in range(N):
    line= list(input().split())
    dict[line[0]]  = line[1:]
print(dict)
