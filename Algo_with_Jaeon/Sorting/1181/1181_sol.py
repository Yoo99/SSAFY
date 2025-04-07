import sys
sys.stdin = open("1181_input.txt")

N = int(input())
words = []
word_length = []
for _ in range(N):
    word = input()
    words.append([len(word), word])
    word_length.append(len(word))
words.sort()
word_length.sort()
for length in set(word_length):
    temp = []
    for word in words:
        if word[0] == length and word[1] not in temp:
            temp.append(word[1])
    temp.sort()
    for b in temp:
        print(b)
