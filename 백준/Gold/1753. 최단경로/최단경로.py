import sys

input = sys.stdin.readline
import heapq


def dijk(start):
    my_heap = []
    dis[start] = 0
    heapq.heappush(my_heap, (0, start))

    while my_heap:
        weight, node = heapq.heappop(my_heap)
        if dis[node] < weight:
            continue
        for n_weight, n_node in my_graph[node]:
            if weight + n_weight < dis[n_node]:
                dis[n_node] = weight + n_weight
                heapq.heappush(my_heap, (weight + n_weight, n_node))


v, e = map(int, input().rstrip().split())
dis = [float('INF') for _ in range(v + 1)]
my_graph = [[] for _ in range(v + 1)]
x = int(input().rstrip())

for _ in range(e):
    start, end, weight = map(int, input().rstrip().split())
    my_graph[start].append((weight, end))

dijk(x)

for i in dis[1:]:
    if i == float('inf'):
        print("INF")
    else:
        print(i)
