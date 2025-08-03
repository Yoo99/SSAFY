import sys
sys.stdin = open("input.txt")

string = list(map(str, input().split()))
dictionary ={}
for char in string:
    if char not in dictionary.keys():
        dictionary[char] = 1
    else:
        dictionary[char] +=1
d = list(dictionary.items())
d.sort(key = lambda x:x[0])
for ele in d:
    print(ele[0], ele[1])