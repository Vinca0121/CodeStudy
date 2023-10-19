import sys
input = sys.stdin.readline
import heapq
import copy
n = int(input().rstrip())

# 첫번쨰 노드를 저장
tree = [[] for _ in range(n+1)]
for _ in range(n):
    data = list(map(int, input().rstrip().split()))
    node = data[0]
    for i in range(1, len(data)-1, 2):
        adjacent = data[i]
        weight = data[i+1]
        tree[node].append([adjacent, weight])

def dfs(start, pre_w):
    global ans
    for node in tree[start]:
        next_node = node[0]
        weight = node[1]
        if not visited[next_node]:
            visited[next_node] = True
            after_w = pre_w + weight
            dfs(next_node, after_w)
    # 갈 수 있는 경우가 없는 경우 (최종 도착지 및 도착지 까지의 거리를 저장)
    if ans[1] < pre_w:
        ans[0] = start
        ans[1] = pre_w


global ans
ans = [0,0]
visited = [0] * (n+1)
visited[1] = True
dfs(1, 0)


# 두번째
visited = [0] * (n+1)
visited[ans[0]] = True
dfs(ans[0],0)

print(ans[1])