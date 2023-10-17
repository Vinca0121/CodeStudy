from collections import deque

def bfs(end):

    while my_que:
        start, ans = my_que.popleft()

        if start == end:
            return ans

        d = (start * 2) % 10000
        s = start - 1 if start != 0 else 9999
        l = (start % 1000) * 10 + start // 1000
        r = (start % 10) * 1000 + start // 10

        for next_oper, next_state in [('D', d), ('S', s), ('L', l), ('R', r)]:
            if not visited[next_state]:
                visited[next_state] = True
                my_que.append((next_state, ans + next_oper))

t = int(input().rstrip())
# 큐 정의
my_que = deque()

for _ in range(t):
    start, end = map(int, input().rstrip().split())
    visited = [False] * 10000
    my_que.append((start, ''))
    visited[start] = True
    result = bfs(end)
    print(result)
    my_que.clear()
