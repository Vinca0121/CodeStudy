import heapq
import sys

input = sys.stdin.readline
import heapq

def dijk(start):
    my_heap = []
    heapq.heappush(my_heap, (0, start))
    dis[start][start] = 0
    while my_heap:
        weight, node = heapq.heappop(my_heap)

        # 기존 비용이 클 때만, 해당 노드로 가는 via를 고려하겠다.
        if dis[start][node] < weight:
            continue

        # 모든 노드에 대해서 검사
        for i in range(1, n+1):
            # 갈 수 있는 노드라면 (간선이 존재)
            if my_graph[node][i] != -1:
                if my_graph[node][i] + weight < dis[start][i]:
                    dis[start][i] = my_graph[node][i] + weight
                    heapq.heappush(my_heap, (my_graph[node][i] + weight, i))

n, m, x = map(int, input().rstrip().split())

dis = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
my_graph = [[-1 for _ in range(n+1)] for _ in range(n+1)]

# 그래프를 채운다.
for _ in range(m):
    start, end, w = map(int, input().rstrip().split())
    my_graph[start][end] = w

for i in range(1, n+1):
    dijk(i)

ans_list = []
for i in range(1,n+1):
    ans_list.append(dis[x][i] + dis[i][x])
print(max(ans_list))
