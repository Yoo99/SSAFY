import sys
sys.stdin = open("input.txt")

n = int(input())
condition = []
for _ in range(n):
    line = list(input().split())
    total1,total2 = 0,0
    single = 0
    if line[0]=='1':
        m1,s1 = map(int, line[1].split(":"))
        total1 += (m1*60 + s1)
        m2,s2 = map(int, line[2].split(":"))
        total2+= (m2 * 60 + s2)
        condition.append([total1, total2])
    if line[0]=='2':
        ans  = 0
        m1,s1 = map(int, line[1].split(":"))
        single += (m1*60 + s1)
        for cond in condition:
            if single in range(cond[0], cond[1]):
                ans+=1
        print(ans)


