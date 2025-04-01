import sys
sys.stdin = open("10814_input.txt")

N = int(input())
people= []
for idx in range(N):
    age, name = input().split()
    people.append([int(age), name, idx])
sorted_people = sorted(people, key = lambda x: (x[0], x[2]))
for age, name,idx in sorted_people:
    print(age, name)
