from collections import deque

MAX = 100001
visited = [0] * MAX

def bfs(start):
    my_que = deque()
    my_que.append((start, 0))
    visited[start] = 1

    while my_que:
        now, length = my_que.popleft()
        if now == end:
            return length

        # 가중치가 0인 간선의 경우 큐의 맨 앞에 넣는다.
        if now * 2 < MAX and not visited[now * 2]:
            visited[now * 2] = 1
            my_que.append((now * 2, length))

        # 한칸 -1하고 x2가 되는 경우가 +1을 2번 하는 것보다 빠르다.
        # 순간이동은 가중치가 0 이기 때문
        if now - 1 >= 0 and not visited[now - 1]:
            visited[now - 1] = 1
            my_que.append((now - 1, length + 1))

        if now + 1 < MAX and not visited[now + 1]:
            visited[now + 1] = 1
            my_que.append((now + 1, length + 1))



start, end = map(int, input().split())
print(bfs(start))
