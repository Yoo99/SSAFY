queue = []
candy = 20
queue.append((1,1)) # 1번이 최초로 1개를 받아간다.
# 마이쮸의 개수만큼 순회를 한다

check = 1   # 현재 queue에 삽입된 사람의 수
while candy>0: # 캔디가 있는 동안
    print(queue)
    person, acc = queue.pop(0)

    if candy - acc <=0:
        result = person
        break
    candy -= acc
    queue.append((person, acc+1))
    queue.append((len(queue)+1, 1))
