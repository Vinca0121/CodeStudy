from collections import deque
import queue
min = float("inf")

str = input()

oper_que = deque()
number_que = queue.Queue()

number = ""
for s in str :
    if s == '+' or s == '-':
        if len(number) > 0:
            number_que.put(int(number))
            number = ""
        oper_que.append(s)
    else:
        number = number + s

number_que.put(int(number))

# print(list(oper_que), list(number_que.queue))
# 첫 값은 확정 +
sum = number_que.get()

while not number_que.empty():
    oper = oper_que.popleft()
    if oper == '+':
        sum += number_que.get()
    # - 가 나오는 순간..
    else :
        while True:
            sum -= number_que.get()
            if number_que.empty():
                break
            oper = oper_que.popleft()
            if oper == '-':
                oper_que.appendleft('-')
                break

print(sum)



