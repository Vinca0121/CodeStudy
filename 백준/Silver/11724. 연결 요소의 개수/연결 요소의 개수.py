from collections import deque
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

visited = [0] * (n + 1)  # 0: 미방문, 1: 방문 중, 2: 방문 완료
graph = [[] for _ in range(n + 1)]  # 인접 행렬로 그래프 구현

for _ in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append(end)
    graph[end].append(start)

cc = 0

for i in range(1, n + 1):
    if visited[i] == 0:
        cc += 1
        my_que = deque([i])
        visited[i] = 1  # 방문 중 표시

        while my_que:
            node = my_que[-1]  # 큐의 마지막 노드 확인 (방문 중 노드)
            found = False

            for s_node in graph[node]:
                if visited[s_node] == 0:
                    my_que.append(s_node)
                    visited[s_node] = 1  # 방문 중 표시
                    found = True
                    break

            if not found:
                my_que.pop()  # 방문 완료 처리
                visited[node] = 2  # 방문 완료 표시

print(cc)
