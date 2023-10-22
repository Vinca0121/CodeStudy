import heapq
import sys

input = sys.stdin.readline

def dijk(start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    dis[start][start] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if dis[start][now] < dist:
            continue
        for i in range(1, n+1):
            if my_graph[now][i] != -1:
                cost = dist + my_graph[now][i]
                if cost < dis[start][i]:
                    dis[start][i] = cost
                    heapq.heappush(heap_data, (cost, i))

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
