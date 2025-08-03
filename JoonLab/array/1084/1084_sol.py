import sys
sys.stdin = open("input.txt")

study= list(input().split())
hours , mins = 0,0
for item in study:
    hr, mm = map(int, item.split(":"))
    hours += hr
    mins +=mm

if mins >=60:
    ph = mins//60
    hours += ph
    mins -= ph * 60

if len(str(mins))<2:
    mins = str(mins).zfill(2)
if len(str(hours))<2:
    hours =str(hours).zfill(2)
print(str(hours) + ":" + str(mins))