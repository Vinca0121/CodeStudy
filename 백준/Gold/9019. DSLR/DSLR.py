from collections import deque

def bfs(end):
    visited = [False] * 10000
    my_que = deque([('D', start, '')])
    visited[start] = True

    while my_que:
        oper, current, path = my_que.popleft()

        if current == end:
            return path

        d = (current * 2) % 10000
        s = current - 1 if current != 0 else 9999
        l = (current % 1000) * 10 + current // 1000
        r = (current % 10) * 1000 + current // 10

        for next_oper, next_state in [('D', d), ('S', s), ('L', l), ('R', r)]:
            if not visited[next_state]:
                visited[next_state] = True
                my_que.append((next_oper, next_state, path + next_oper))

t = int(input().rstrip())

for _ in range(t):
    start, end = map(int, input().rstrip().split())
    result = bfs(end)
    print(result)
