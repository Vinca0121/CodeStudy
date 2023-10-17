from collections import deque

def bfs(end, visited):

    while my_que:
        start, ans = my_que.popleft()

        if start == end:
            return ans

        # 첫 연산에서 4개의 연산의 경우를 모두 실행 (BFS)
        # 각 연산을 취했을 때의 값을 계산
        d_num = (start * 2) % 10000
        s_num = start - 1 if start != 0 else 9999
        l_num = (start % 1000) * 10 + start // 1000
        r_num = (start % 10) * 1000 + start // 10

        # 각 연산의 값을 큐에 추가
        if not visited[d_num]:
            visited[d_num] = True
            my_que.append((d_num, ans + 'D'))

        if not visited[s_num]:
            visited[s_num] = True
            my_que.append((s_num, ans + 'S'))

        if not visited[l_num]:
            visited[l_num] = True
            my_que.append((l_num, ans + 'L'))

        if not visited[r_num]:
            visited[r_num] = True
            my_que.append((r_num, ans + 'R'))


t = int(input().rstrip())
# 큐 정의
my_que = deque()

for _ in range(t):
    start, end = map(int, input().rstrip().split())
    visited = [False] * 10000
    visited[start] = True
    my_que.append((start, ''))
    print(bfs(end, visited))
    my_que.clear()
