arr = ['O','X']
path = []
name = ['Min','Co','Tim']
def print_name():
    for i in range(3):
        if path[i] =='O':
            print(name[i], end = ' ')
    print()
def run(lev):
    if lev == 3:
        # print(path)
        print_name()
        return
    for i in range(2):
        path.append(arr[i])
        run(lev+1)
        path.pop()
run(0)

arr = ['A','B','C','D','E']
n = len(arr)
total_subset = []
for i in range(1<<n):
    subset = []
    for j in range(n):
        if i & (1<<j):
            subset.append(arr[j])
    total_subset.append(subset)
final = 0
for set in total_subset:
    if len(set)>=2:
        final +=1
print(final)
