card = ['A','J','Q','K']
path = []
result = 0

def count_three():
    if path[0] ==path[1] ==path[2]:return True
    if path[1]==path[2]==path[3]: return True
    if path[2]==path[3]==path[4]:return True
    return False

def recur(cnt):
    global result
    if cnt ==5:
        if count_three():
            result +=1
            print(path)
        return
    for idx in range(4):
        path.append(card[idx])
        recur(cnt+1)
        path.pop()

recur(0)